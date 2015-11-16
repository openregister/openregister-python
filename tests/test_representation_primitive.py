from openregister import Item


def test_empty_item_as_primitive():
    item = Item()
    data = item.primitive
    assert data == {}


def test_empty_item_from_primitive():
    item = Item()
    item.primitive = {}
    assert item.primitive == {}


def test_ignore_private_as_primitive():
    item = Item()
    item._zero = "to be removed"
    item.one = "one value"
    item._two = "should be removed"
    item.two = "two value"
    item._three = "three"

    data = item.primitive
    assert data == ({"one": "one value", "two": "two value"})


def test_postaladdress_as_primitive():
    item = Item()
    item.streetAddress = "Aviation House, 125 Kingsway"
    item.addressLocality = "Holborn"
    item.addressRegion = "London"
    item.postcode = "WC2B 6NH"
    item.addressCountry = "GB"

    assert item.primitive == {
        'addressCountry': 'GB',
        'addressLocality': 'Holborn',
        'addressRegion': 'London',
        'postcode': 'WC2B 6NH',
        'streetAddress': 'Aviation House, 125 Kingsway'}


def test_postaladdress_from_primitive():
    item = Item()
    item.primitive = {
        'addressCountry': 'GB',
        'addressLocality': 'Holborn',
        'addressRegion': 'London',
        'postcode': 'WC2B 6NH',
        'streetAddress': 'Aviation House, 125 Kingsway'}

    assert item.streetAddress == "Aviation House, 125 Kingsway"
    assert item.addressLocality == "Holborn"
    assert item.addressRegion == "London"
    assert item.postcode == "WC2B 6NH"
    assert item.addressCountry == "GB"


def test_set_of_tags_as_primitive():
    item = Item(name='foo', fields={'z', 'b', 'c', 'z'})
    assert item.primitive == {
        'fields': ['b', 'c', 'z'],
        'name': 'foo'}


def test_set_of_tags_from_primitive():
    item = Item()
    item.primitive = {
        'fields': ['a', 'b', 'c'],
        'name': 'foo'}
    assert item.name == 'foo'
    assert item.fields == ['a', 'b', 'c']
