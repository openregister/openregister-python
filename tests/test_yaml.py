from thingstance import Thing


def test_thing_as_json():
    thing = Thing()
    data = thing.yaml
    assert data == ('{}\n')

    thing.streetAddress = "Aviation House, 125 Kingsway"
    thing.addressLocality = "Holborn"
    thing.addressRegion = "London"
    thing.postcode = "WC2B 6NH"
    thing.addressCountry = "GB"

    data = thing.yaml
    print(data)
    assert data == ('addressCountry: GB\n'
                    'addressLocality: Holborn\n'
                    'addressRegion: London\n'
                    'postcode: WC2B 6NH\n'
                    'streetAddress: Aviation House, 125 Kingsway\n')
