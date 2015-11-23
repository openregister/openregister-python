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

    assert item.foo == "Foo Value"
    assert item.bar == "Bar Value"
    assert item['bar'] == "Bar Value"
    assert item['kebab-value'] == "A Kebab"

    assert item.get('kebab-value') == "A Kebab"
    assert item.get('a-missing-value') is None

    item.set('another', "Another Value")
    assert item.another == "Another Value"
