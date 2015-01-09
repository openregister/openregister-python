import pytest
from thingstance import Thing


def test_new_empty_thing():
    thing = Thing()

    with pytest.raises(AttributeError):
        thing.zog


def test_new_thing_from_params():
    thing = Thing(foo="Foo Value", bar="Bar Value")
    assert thing.foo == "Foo Value"
    assert thing.bar == "Bar Value"

    with pytest.raises(AttributeError):
        thing.zog
