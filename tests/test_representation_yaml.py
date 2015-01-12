from thingstance import Thing


def test_empty_thing_as_yaml():
    thing = Thing()
    data = thing.yaml
    assert data == ('{}\n')


def test_empty_thing_from_yaml():
    thing = Thing()
    thing.yaml = ('{}')
    assert thing.yaml == ('{}\n')


def test_postaladdress_as_yaml():
    thing = Thing()
    thing.streetAddress = "Aviation House, 125 Kingsway"
    thing.addressLocality = "Holborn"
    thing.addressRegion = "London"
    thing.postcode = "WC2B 6NH"
    thing.addressCountry = "GB"

    data = thing.yaml
    assert data == ('addressCountry: GB\n'
                    'addressLocality: Holborn\n'
                    'addressRegion: London\n'
                    'postcode: WC2B 6NH\n'
                    'streetAddress: Aviation House, 125 Kingsway\n')


def test_postaladdress_from_yaml():
    thing = Thing()
    thing.yaml = ('addressCountry: GB\n'
                  'addressLocality: Holborn\n'
                  'addressRegion: London\n'
                  'postcode: WC2B 6NH\n'
                  'streetAddress: Aviation House, 125 Kingsway\n')

    assert thing.streetAddress == "Aviation House, 125 Kingsway"
    assert thing.addressLocality == "Holborn"
    assert thing.addressRegion == "London"
    assert thing.postcode == "WC2B 6NH"
    assert thing.addressCountry == "GB"


def test_set_of_tags_as_yaml():
    thing = Thing(name='foo', fields={'z', 'b', 'c', 'z'})
    data = thing.yaml
    assert data == ('fields: !!set\n'
                    '  b: null\n'
                    '  c: null\n'
                    '  z: null\n'
                    'name: foo\n')


def test_set_of_tags_from_yaml():
    thing = Thing()
    thing.yaml = ('fields: !!set\n'
                  '  b: null\n'
                  '  c: null\n'
                  '  z: null\n'
                  'name: foo\n')
    assert thing.name == "foo"
    assert thing.fields == {'b', 'c', 'z'}
