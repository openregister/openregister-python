import pytest
from openregister import Item


def test_new_empty_item():
    item = Item()

    with pytest.raises(AttributeError):
        item.zog


def test_new_item_from_params():
    item = Item(foo="Foo Value", bar="Bar Value")
    assert item.foo == "Foo Value"
    assert item.bar == "Bar Value"

    with pytest.raises(AttributeError):
        item.zog


def test_item_sorted_keys():
    item = Item(c="two", a="zero", d="three", b="one", e="four")
    keys = item.keys
    assert keys[0] == "a"
    assert keys[1] == "b"
    assert keys[2] == "c"
    assert keys[3] == "d"
    assert keys[4] == "e"


def test_item_assignment():
    item = Item()
    item.foo = "Foo Value"
    item.bar = "Bar Value"
    item['kebab-value'] = "A Kebab"
    item['empty'] = ''

    assert item.foo == "Foo Value"
    assert item.bar == "Bar Value"
    assert item['bar'] == "Bar Value"
    assert item['kebab-value'] == "A Kebab"

    assert item.get('kebab-value') == "A Kebab"
    assert item.get('a-missing-value') is None
    assert item.get('empty') is None

    item.set('another', "Another Value")
    assert item.another == "Another Value"


def test_empty_item_as_primitive():
    item = Item()
    data = item.primitive
    assert data == {}


def test_empty_item_from_primitive():
    item = Item()
    item.primitive = {}
    assert item.primitive == {}


def test_empty_field_is_missing():
    item = Item()
    item.primitive = {"empty-field": "", "field": "bar"}
    assert item.primitive == {"field": "bar"}


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
