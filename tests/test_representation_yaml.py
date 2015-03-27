from entry import Entry
from entry.representations.yaml import content_type


def test_yaml_content_type():
    assert content_type == "application/yaml"


def test_empty_entry_as_yaml():
    entry = Entry()
    data = entry.yaml
    assert data == ('{}\n')


def test_empty_entry_from_yaml():
    entry = Entry()
    entry.yaml = ('{}')
    assert entry.yaml == ('{}\n')


def test_postaladdress_as_yaml():
    entry = Entry()
    entry.streetAddress = "Aviation House, 125 Kingsway"
    entry.addressLocality = "Holborn"
    entry.addressRegion = "London"
    entry.postcode = "WC2B 6NH"
    entry.addressCountry = "GB"

    data = entry.yaml
    assert data == ('addressCountry: GB\n'
                    'addressLocality: Holborn\n'
                    'addressRegion: London\n'
                    'postcode: WC2B 6NH\n'
                    'streetAddress: Aviation House, 125 Kingsway\n')


def test_postaladdress_from_yaml():
    entry = Entry()
    entry.yaml = ('addressCountry: GB\n'
                  'addressLocality: Holborn\n'
                  'addressRegion: London\n'
                  'postcode: WC2B 6NH\n'
                  'streetAddress: Aviation House, 125 Kingsway\n')

    assert entry.streetAddress == "Aviation House, 125 Kingsway"
    assert entry.addressLocality == "Holborn"
    assert entry.addressRegion == "London"
    assert entry.postcode == "WC2B 6NH"
    assert entry.addressCountry == "GB"


def test_set_of_tags_as_yaml():
    entry = Entry(name='foo', fields={'z', 'b', 'c', 'z'})
    data = entry.yaml
    assert data == ('fields:\n'
                    '- b\n'
                    '- c\n'
                    '- z\n'
                    'name: foo\n')


def test_set_of_tags_from_yaml():
    entry = Entry()
    entry.yaml = ('fields:\n'
                  '  - b\n'
                  '  - c\n'
                  '  - z\n'
                  'name: foo\n')
    assert entry.name == "foo"
    assert entry.fields == ['b', 'c', 'z']
