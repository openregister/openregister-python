from openregister import Item
from openregister.representations.txt import content_type


def test_txt_content_type():
    assert content_type == "text/plain; charset=utf-8"


def test_empty_item_as_txt():
    item = Item()
    data = item.txt
    assert data == ('{}\n')


def test_empty_item_from_txt():
    item = Item()
    item.txt = ('{}')
    assert item.txt == ('{}\n')


def test_postaladdress_as_txt():
    item = Item()
    item.streetAddress = "Aviation House, 125 Kingsway"
    item.addressLocality = "Holborn"
    item.addressRegion = "London"
    item.postcode = "WC2B 6NH"
    item.addressCountry = "GB"

    data = item.txt
    assert data == ('addressCountry: GB\n'
                    'addressLocality: Holborn\n'
                    'addressRegion: London\n'
                    'postcode: WC2B 6NH\n'
                    'streetAddress: Aviation House, 125 Kingsway\n')


def test_postaladdress_from_txt():
    item = Item()
    item.txt = ('addressCountry: GB\n'
                'addressLocality: Holborn\n'
                'addressRegion: London\n'
                'postcode: WC2B 6NH\n'
                'streetAddress: Aviation House, 125 Kingsway\n')

    assert item.streetAddress == "Aviation House, 125 Kingsway"
    assert item.addressLocality == "Holborn"
    assert item.addressRegion == "London"
    assert item.postcode == "WC2B 6NH"
    assert item.addressCountry == "GB"


def test_set_of_tags_as_txt():
    item = Item(name='foo', fields={'z', 'b', 'c', 'z'})
    data = item.txt
    assert data == ('fields:\n'
                    '- b\n'
                    '- c\n'
                    '- z\n'
                    'name: foo\n')


def test_set_of_tags_from_txt():
    item = Item()
    item.txt = ('fields:\n'
                '  - b\n'
                '  - c\n'
                '  - z\n'
                'name: foo\n')
    assert item.name == "foo"
    assert item.fields == ['b', 'c', 'z']
