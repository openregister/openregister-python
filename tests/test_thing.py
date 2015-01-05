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
    # $ /bin/echo '{}\c' > x
    # $ git add x ; git commit -m"x" x
    # $ git hash-object x
    #
    assert thing.uid == "9e26dfeeb6e641a33dae4961196235bdb965b21b"

    #
    # $ /bin/echo '{"foo": "Foo Value"}\c' > y
    # $ git add y ; git commit -m"y" y
    # $ git hash-object y
    #
    thing.foo = "Foo Value"
    assert thing.json == '{"foo": "Foo Value"}'
    assert thing.uid == "52664e0e405d51dad2d6c0e2979b4e1377e42abc"

    #
    # $ /bin/echo '{"bar": "こんにちは、元気ですか", "foo": "Foo Value"}\c' > z
    # $ git add z ; git commit -m"z" z
    # $ git hash-object z
    #
    thing.bar = "こんにちは、元気ですか"
    assert thing.json == '{"bar": "こんにちは、元気ですか", "foo": "Foo Value"}'
    assert thing.uid == "9e8ef586772127778e1a3ac05bfd16bd20c5e57a"
