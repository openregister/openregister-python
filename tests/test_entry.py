import pytest
from entry import Entry


def test_new_empty_entry():
    entry = Entry()

    with pytest.raises(AttributeError):
        entry.zog


def test_new_entry_from_params():
    entry = Entry(foo="Foo Value", bar="Bar Value")
    assert entry.foo == "Foo Value"
    assert entry.bar == "Bar Value"

    with pytest.raises(AttributeError):
        entry.zog


def test_entry_sorted_keys():
    entry = Entry(c="two", a="zero", d="three", b="one", e="four")
    keys = entry.keys
    assert keys[0] == "a"
    assert keys[1] == "b"
    assert keys[2] == "c"
    assert keys[3] == "d"
    assert keys[4] == "e"
