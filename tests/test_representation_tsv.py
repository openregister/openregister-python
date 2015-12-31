from openregister import Item
from openregister.representations.tsv import content_type


def test_tsv_content_type():
    assert content_type == "text/tab-separated-values; charset=utf-8"


def test_empty_item_as_tsv():
    item = Item()
    assert item.tsv == ''


def test_simple_as_tsv():
    item = Item()
    item.a = "A value"
    assert item.tsv == (
        'a\n'
        'A value\n'
    )


def test_newlines_as_tsv():
    item = Item()
    item.a = "A value:\ncontaining a newline"
    assert item.tsv == (
        'a\n'
        'A value:\\ncontaining a newline\n'
    )


def test_newlines_from_tsv():
    item = Item()
    item.tsv = (
        'a\n'
        'A value:\\ncontaining a newline\n'
    )
    assert item.a == 'A value:\ncontaining a newline'


def test_list_as_tsv():
    item = Item()
    item.a = ["one value", "two value", "three value"]

    assert item.tsv == (
        'a\n'
        'one value;two value;three value\n'
    )


def test_ignore_private_as_tsv():
    item = Item()
    item._zero = "to be removed"
    item.one = "one value"
    item._two = "should be removed"
    item.two = "two value"
    item._three = "three"

    assert item.tsv == (
        'one\ttwo\n'
        'one value\ttwo value\n'
    )


def test_postaladdress_as_tsv():
    item = Item()
    item.streetAddress = "Aviation House, 125 Kingsway"
    item.addressLocality = "Holborn"
    item.addressRegion = "London"
    item.postcode = "WC2B 6NH"
    item.addressCountry = "GB"

    data = item.tsv
    assert data == (
        'addressCountry\taddressLocality\taddressRegion\tpostcode\tstreetAddress\n'  # NOQA
        'GB\tHolborn\tLondon\tWC2B 6NH\tAviation House, 125 Kingsway\n'              # NOQA
    )


def test_postaladdress_from_tsv():
    item = Item()
    item.tsv = (
        'addressCountry\taddressLocality\taddressRegion\tpostcode\tstreetAddress\n'  # NOQA
        'GB\tHolborn\tLondon\tWC2B 6NH\tAviation House, 125 Kingsway\n'              # NOQA
    )

    assert item.streetAddress == "Aviation House, 125 Kingsway"
    assert item.addressLocality == "Holborn"
    assert item.addressRegion == "London"
    assert item.postcode == "WC2B 6NH"
    assert item.addressCountry == "GB"
