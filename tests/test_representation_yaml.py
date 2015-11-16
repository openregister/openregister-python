from openregister.item import Item
from openregister.representations.yaml import content_type


def test_yaml_content_type():
    assert content_type == "application/yaml"


def test_empty_item_as_yaml():
    item = Item()
    data = item.yaml
    assert data == ('{}\n')


def test_empty_item_from_yaml():
    item = Item()
    item.yaml = ('{}')
    assert item.yaml == ('{}\n')


def test_postaladdress_as_yaml():
    item = Item()
    item.streetAddress = "Aviation House, 125 Kingsway"
    item.addressLocality = "Holborn"
    item.addressRegion = "London"
    item.postcode = "WC2B 6NH"
    item.addressCountry = "GB"

    data = item.yaml
    assert data == ('addressCountry: GB\n'
                    'addressLocality: Holborn\n'
                    'addressRegion: London\n'
                    'postcode: WC2B 6NH\n'
                    'streetAddress: Aviation House, 125 Kingsway\n')


def test_postaladdress_from_yaml():
    item = Item()
    item.yaml = ('addressCountry: GB\n'
                 'addressLocality: Holborn\n'
                 'addressRegion: London\n'
                 'postcode: WC2B 6NH\n'
                 'streetAddress: Aviation House, 125 Kingsway\n')

    assert item.streetAddress == "Aviation House, 125 Kingsway"
    assert item.addressLocality == "Holborn"
    assert item.addressRegion == "London"
    assert item.postcode == "WC2B 6NH"
    assert item.addressCountry == "GB"


def test_set_of_tags_as_yaml():
    item = Item(name='foo', fields={'z', 'b', 'c', 'z'})
    data = item.yaml
    assert data == ('fields:\n'
                    '- b\n'
                    '- c\n'
                    '- z\n'
                    'name: foo\n')


def test_set_of_tags_from_yaml():
    item = Item()
    item.yaml = ('fields:\n'
                 '  - b\n'
                 '  - c\n'
                 '  - z\n'
                 'name: foo\n')
    assert item.name == "foo"
    assert item.fields == ['b', 'c', 'z']
