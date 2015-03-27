from entry import Entry
from entry.representations.txt import content_type


def test_txt_content_type():
    assert content_type == "text/plain; charset=utf-8"


def test_empty_entry_as_txt():
    entry = Entry()
    data = entry.txt
    assert data == ('{}\n')


def test_empty_entry_from_txt():
    entry = Entry()
    entry.txt = ('{}')
    assert entry.txt == ('{}\n')


def test_postaladdress_as_txt():
    entry = Entry()
    entry.streetAddress = "Aviation House, 125 Kingsway"
    entry.addressLocality = "Holborn"
    entry.addressRegion = "London"
    entry.postcode = "WC2B 6NH"
    entry.addressCountry = "GB"

    data = entry.txt
    assert data == ('addressCountry: GB\n'
                    'addressLocality: Holborn\n'
                    'addressRegion: London\n'
                    'postcode: WC2B 6NH\n'
                    'streetAddress: Aviation House, 125 Kingsway\n')


def test_postaladdress_from_txt():
    entry = Entry()
    entry.txt = ('addressCountry: GB\n'
                 'addressLocality: Holborn\n'
                 'addressRegion: London\n'
                 'postcode: WC2B 6NH\n'
                 'streetAddress: Aviation House, 125 Kingsway\n')

    assert entry.streetAddress == "Aviation House, 125 Kingsway"
    assert entry.addressLocality == "Holborn"
    assert entry.addressRegion == "London"
    assert entry.postcode == "WC2B 6NH"
    assert entry.addressCountry == "GB"


def test_set_of_tags_as_txt():
    entry = Entry(name='foo', fields={'z', 'b', 'c', 'z'})
    data = entry.txt
    assert data == ('fields:\n'
                    '- b\n'
                    '- c\n'
                    '- z\n'
                    'name: foo\n')


def test_set_of_tags_from_txt():
    entry = Entry()
    entry.txt = ('fields:\n'
                 '  - b\n'
                 '  - c\n'
                 '  - z\n'
                 'name: foo\n')
    assert entry.name == "foo"
    assert entry.fields == ['b', 'c', 'z']
