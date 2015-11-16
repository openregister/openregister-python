import pytest
from openregister import Item
from openregister.representations.json import content_type


def test_json_content_type():
    assert content_type == "application/json"


def test_empty_item_as_json():
    item = Item()
    data = item.json
    assert data == '{}'


def test_empty_item_from_json():
    item = Item()
    item.json = ('{}')
    assert item.json == ('{}')


def test_empty_item_from_json_with_whitespace():
    item = Item()

    item.json = ('{}')
    assert item.json == ('{}')

    item.json = ('   {  }')
    assert item.json == ('{}')


def test_unserializable__as_json():
    item = Item(name='foo', unserializable=pytest)
    with pytest.raises(AttributeError):
        item.json


def test_ignore_private_as_json():
    item = Item()
    item._zero = "to be removed"
    item.one = "one value"
    item._two = "should be removed"
    item.two = "two value"
    item._three = "three"

    data = item.json
    assert data == ('{"one":"one value","two":"two value"}')


def test_postaladdress_as_json():
    item = Item()
    item.streetAddress = "Aviation House, 125 Kingsway"
    item.addressLocality = "Holborn"
    item.addressRegion = "London"
    item.postcode = "WC2B 6NH"
    item.addressCountry = "GB"

    data = item.json
    assert data == ('{"addressCountry":"GB",'
                    '"addressLocality":"Holborn",'
                    '"addressRegion":"London",'
                    '"postcode":"WC2B 6NH",'
                    '"streetAddress":"Aviation House, 125 Kingsway"}')


def test_postaladdress_from_json():
    item = Item()
    item.json = ('{"addressCountry":"GB",'
                 '"addressLocality":"Holborn",'
                 '"addressRegion":"London",'
                 '"postcode":"WC2B 6NH",'
                 '"streetAddress":"Aviation House, 125 Kingsway"}')

    assert item.streetAddress == "Aviation House, 125 Kingsway"
    assert item.addressLocality == "Holborn"
    assert item.addressRegion == "London"
    assert item.postcode == "WC2B 6NH"
    assert item.addressCountry == "GB"


def test_set_of_tags_as_json():
    item = Item(name='foo', fields={'a', 'b', 'c', 'a'})
    data = item.json
    assert data == ('{"fields":["a","b","c"],"name":"foo"}')


def test_set_of_tags_from_json():
    item = Item()
    item.json = ('{"fields":["a","b","c"],"name":"foo"}')
    assert item.name == 'foo'
    assert item.fields == ['a', 'b', 'c']
