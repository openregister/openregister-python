from thingstance import Thing


def test_empty_thing_as_json():
    thing = Thing()
    data = thing.json
    assert data == '{}'


def test_postaladdress_as_json():
    thing = Thing()
    thing.streetAddress = "Aviation House, 125 Kingsway"
    thing.addressLocality = "Holborn"
    thing.addressRegion = "London"
    thing.postcode = "WC2B 6NH"
    thing.addressCountry = "GB"

    data = thing.json
    assert data == ('{"addressCountry": "GB",'
                    ' "addressLocality": "Holborn",'
                    ' "addressRegion": "London",'
                    ' "postcode": "WC2B 6NH",'
                    ' "streetAddress": "Aviation House, 125 Kingsway"}')


def test_set_of_tags_as_json():
    thing = Thing(name='foo', fields={'a', 'b', 'c', 'a'})
    data = thing.json
    assert data == ('{"fields": ["a", "b", "c"], "name": "foo"}')
