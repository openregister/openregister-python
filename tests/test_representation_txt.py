from thingstance import Thing
from thingstance.representations.txt import content_type


def test_txt_content_type():
    assert content_type == "text/plain; charset=utf-8"


def test_empty_thing_as_txt():
    thing = Thing()
    data = thing.txt
    assert data == ('{}\n')


def test_empty_thing_from_txt():
    thing = Thing()
    thing.txt = ('{}')
    assert thing.txt == ('{}\n')


def test_postaladdress_as_txt():
    thing = Thing()
    thing.streetAddress = "Aviation House, 125 Kingsway"
    thing.addressLocality = "Holborn"
    thing.addressRegion = "London"
    thing.postcode = "WC2B 6NH"
    thing.addressCountry = "GB"

    data = thing.txt
    assert data == ('addressCountry: GB\n'
                    'addressLocality: Holborn\n'
                    'addressRegion: London\n'
                    'postcode: WC2B 6NH\n'
                    'streetAddress: Aviation House, 125 Kingsway\n')


def test_postaladdress_from_txt():
    thing = Thing()
    thing.txt = ('addressCountry: GB\n'
                 'addressLocality: Holborn\n'
                 'addressRegion: London\n'
                 'postcode: WC2B 6NH\n'
                 'streetAddress: Aviation House, 125 Kingsway\n')

    assert thing.streetAddress == "Aviation House, 125 Kingsway"
    assert thing.addressLocality == "Holborn"
    assert thing.addressRegion == "London"
    assert thing.postcode == "WC2B 6NH"
    assert thing.addressCountry == "GB"


def test_set_of_tags_as_txt():
    thing = Thing(name='foo', fields={'z', 'b', 'c', 'z'})
    data = thing.txt
    assert data == ('fields:\n'
                    '- b\n'
                    '- c\n'
                    '- z\n'
                    'name: foo\n')


def test_set_of_tags_from_txt():
    thing = Thing()
    thing.txt = ('fields:\n'
                 '  - b\n'
                 '  - c\n'
                 '  - z\n'
                 'name: foo\n')
    assert thing.name == "foo"
    assert thing.fields == ['b', 'c', 'z']
