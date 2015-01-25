from thingstance import Thing
from thingstance.representations.tsv import content_type


def test_tsv_content_type():
    assert content_type == "text/tab-separated-values; charset=utf-8"


def test_empty_thing_as_tsv():
    thing = Thing()
    assert thing.tsv == ''


def test_simple_as_tsv():
    thing = Thing()
    thing.a = "A value"
    assert thing.tsv == (
        'a\n'
        'A value\n'
    )


def test_ignore_private_as_tsv():
    thing = Thing()
    thing._zero = "to be removed"
    thing.one = "one value"
    thing._two = "should be removed"
    thing.two = "two value"
    thing._three = "three"

    assert thing.tsv == (
        'one\ttwo\n'
        'one value\ttwo value\n'
    )


def test_postaladdress_as_tsv():
    thing = Thing()
    thing.streetAddress = "Aviation House, 125 Kingsway"
    thing.addressLocality = "Holborn"
    thing.addressRegion = "London"
    thing.postcode = "WC2B 6NH"
    thing.addressCountry = "GB"

    data = thing.tsv
    assert data == (
        'addressCountry\taddressLocality\taddressRegion\tpostcode\tstreetAddress\n'  # NOQA
        'GB\tHolborn\tLondon\tWC2B 6NH\tAviation House, 125 Kingsway\n'              # NOQA
    )


def test_postaladdress_from_tsv():
    thing = Thing()
    thing.tsv = (
        'addressCountry\taddressLocality\taddressRegion\tpostcode\tstreetAddress\n'  # NOQA
        'GB\tHolborn\tLondon\tWC2B 6NH\tAviation House, 125 Kingsway\n'              # NOQA
    )

    assert thing.streetAddress == "Aviation House, 125 Kingsway"
    assert thing.addressLocality == "Holborn"
    assert thing.addressRegion == "London"
    assert thing.postcode == "WC2B 6NH"
    assert thing.addressCountry == "GB"
