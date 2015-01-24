from thingstance import Thing


def test_empty_thing_as_primitive():
    thing = Thing()
    data = thing.primitive
    assert data == {}


def test_empty_thing_from_primitive():
    thing = Thing()
    thing.primitive = {}
    assert thing.primitive == {}


def test_ignore_private_as_primitive():
    thing = Thing()
    thing._zero = "to be removed"
    thing.one = "one value"
    thing._two = "should be removed"
    thing.two = "two value"
    thing._three = "three"

    data = thing.primitive
    assert data == ({"one": "one value", "two": "two value"})


def test_postaladdress_as_primitive():
    thing = Thing()
    thing.streetAddress = "Aviation House, 125 Kingsway"
    thing.addressLocality = "Holborn"
    thing.addressRegion = "London"
    thing.postcode = "WC2B 6NH"
    thing.addressCountry = "GB"

    assert thing.primitive == {
        'addressCountry': 'GB',
        'addressLocality': 'Holborn',
        'addressRegion': 'London',
        'postcode': 'WC2B 6NH',
        'streetAddress': 'Aviation House, 125 Kingsway'}


def test_postaladdress_from_primitive():
    thing = Thing()
    thing.primitive = {
        'addressCountry': 'GB',
        'addressLocality': 'Holborn',
        'addressRegion': 'London',
        'postcode': 'WC2B 6NH',
        'streetAddress': 'Aviation House, 125 Kingsway'}

    assert thing.streetAddress == "Aviation House, 125 Kingsway"
    assert thing.addressLocality == "Holborn"
    assert thing.addressRegion == "London"
    assert thing.postcode == "WC2B 6NH"
    assert thing.addressCountry == "GB"


def test_set_of_tags_as_primitive():
    thing = Thing(name='foo', fields={'z', 'b', 'c', 'z'})
    assert thing.primitive == {
        'fields': ['b', 'c', 'z'],
        'name': 'foo'}


def test_set_of_tags_from_primitive():
    thing = Thing()
    thing.primitive = {
        'fields': ['a', 'b', 'c'],
        'name': 'foo'}
    assert thing.name == 'foo'
    assert thing.fields == ['a', 'b', 'c']
