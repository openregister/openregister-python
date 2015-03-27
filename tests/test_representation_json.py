import pytest
from entry import Entry
from entry.representations.json import content_type


def test_json_content_type():
    assert content_type == "application/json"


def test_empty_entry_as_json():
    entry = Entry()
    data = entry.json
    assert data == '{}\n'


def test_empty_entry_from_json():
    entry = Entry()
    entry.json = ('{}')
    assert entry.json == ('{}\n')


def test_empty_entry_from_json_with_whitespace():
    entry = Entry()

    entry.json = ('{}\n')
    assert entry.json == ('{}\n')

    entry.json = ('   {  }\n\n')
    assert entry.json == ('{}\n')


def test_unserializable__as_json():
    entry = Entry(name='foo', unserializable=pytest)
    with pytest.raises(AttributeError):
        entry.json


def test_ignore_private_as_json():
    entry = Entry()
    entry._zero = "to be removed"
    entry.one = "one value"
    entry._two = "should be removed"
    entry.two = "two value"
    entry._three = "three"

    data = entry.json
    assert data == ('{"one": "one value", "two": "two value"}\n')


def test_postaladdress_as_json():
    entry = Entry()
    entry.streetAddress = "Aviation House, 125 Kingsway"
    entry.addressLocality = "Holborn"
    entry.addressRegion = "London"
    entry.postcode = "WC2B 6NH"
    entry.addressCountry = "GB"

    data = entry.json
    assert data == ('{"addressCountry": "GB",'
                    ' "addressLocality": "Holborn",'
                    ' "addressRegion": "London",'
                    ' "postcode": "WC2B 6NH",'
                    ' "streetAddress": "Aviation House, 125 Kingsway"}\n')


def test_postaladdress_from_json():
    entry = Entry()
    entry.json = ('{"addressCountry": "GB",'
                  ' "addressLocality": "Holborn",'
                  ' "addressRegion": "London",'
                  ' "postcode": "WC2B 6NH",'
                  ' "streetAddress": "Aviation House, 125 Kingsway"}\n')

    assert entry.streetAddress == "Aviation House, 125 Kingsway"
    assert entry.addressLocality == "Holborn"
    assert entry.addressRegion == "London"
    assert entry.postcode == "WC2B 6NH"
    assert entry.addressCountry == "GB"


def test_set_of_tags_as_json():
    entry = Entry(name='foo', fields={'a', 'b', 'c', 'a'})
    data = entry.json
    assert data == ('{"fields": ["a", "b", "c"], "name": "foo"}\n')


def test_set_of_tags_from_json():
    entry = Entry()
    entry.json = ('{"fields": ["a", "b", "c"], "name": "foo"}')
    assert entry.name == 'foo'
    assert entry.fields == ['a', 'b', 'c']
