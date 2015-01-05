import pytest

from thingstance import Thing


def test_new_thing():
    thing = Thing()

    with pytest.raises(AttributeError):
        thing.zog

    thing = Thing(foo="Foo Value", bar="Bar Value")
    assert thing.foo == "Foo Value"
    assert thing.bar == "Bar Value"

    with pytest.raises(AttributeError):
        thing.zog


def test_thing_as_json():
    thing = Thing()
    data = thing.json
    assert data == '{}'

    thing.streetAddress = "Aviation House, 125 Kingsway"
    thing.addressLocality = "Holborn"
    thing.addressRegion = "London"
    thing.postcode = "WC2B 6NH"
    thing.addressCountry = "GB"

    data = thing.json
    assert data == ('{"addressCountry": "GB",'
                    ' "addressLocality": "Holborn",'
                    ' "addressRegion": "London",'
                    ' "postcode": "WC2B 6NH",'
                    ' "streetAddress": "Aviation House, 125 Kingsway"}')


def test_thing_uid():
    thing = Thing()

    #
    # $ echo "{}\c" > x
    # $ git add x ; git commit -m"x" x
    # $ git hash-object x
    # 9e26dfeeb6e641a33dae4961196235bdb965b21b
    #
    assert thing.uid == "9e26dfeeb6e641a33dae4961196235bdb965b21b"
