import pytest
from openregister import Item
from openregister.representations.jsonl import content_type


def test_jsonl_content_type():
    assert content_type == "application/json-l"


def test_empty_item_as_jsonl():
    item = Item()
    data = item.jsonl
    assert data == '{}'


def test_empty_item_from_jsonl():
    item = Item()
    item.jsonl = ('{}')
    assert item.jsonl == ('{}')


def test_unserializable__as_jsonl():
    item = Item(name='foo', unserializable=pytest)
    with pytest.raises(AttributeError):
        item.jsonl


def test_postaladdress_as_jsonl():
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


def test_postaladdress_from_jsonl():
    item = Item()
    item.jsonl = ('{"addressCountry":"GB",'
                  '"addressLocality":"Holborn",'
                  '"addressRegion":"London",'
                  '"postcode":"WC2B 6NH",'
                  '"streetAddress":"Aviation House, 125 Kingsway"}')

    assert item.streetAddress == "Aviation House, 125 Kingsway"
    assert item.addressLocality == "Holborn"
    assert item.addressRegion == "London"
    assert item.postcode == "WC2B 6NH"
    assert item.addressCountry == "GB"


def test_set_of_tags_as_jsonl():
    item = Item(name='foo', fields={'a', 'b', 'c', 'a'})
    data = item.json
    assert data == ('{"fields":["a","b","c"],"name":"foo"}')


def test_set_of_tags_from_jsonl():
    item = Item()
    item.jsonl = ('{"fields":["a","b","c"],"name":"foo"}')
    assert item.name == 'foo'
    assert item.fields == ['a', 'b', 'c']
