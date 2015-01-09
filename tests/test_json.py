from thingstance import Thing


def test_thing_as_json():
    thing = Thing()
    data = thing.json
    assert data == '{}'

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
