from entry import Entry
from entry.representations.tsv import content_type


def test_tsv_content_type():
    assert content_type == "text/tab-separated-values; charset=utf-8"


def test_empty_entry_as_tsv():
    entry = Entry()
    assert entry.tsv == ''


def test_simple_as_tsv():
    entry = Entry()
    entry.a = "A value"
    assert entry.tsv == (
        'a\n'
        'A value\n'
    )


def test_newlines_as_tsv():
    entry = Entry()
    entry.a = "A value:\ncontaining a newline"
    assert entry.tsv == (
        'a\n'
        'A value:\\ncontaining a newline\n'
    )


def test_newlines_from_tsv():
    entry = Entry()
    entry.tsv = (
        'a\n'
        'A value:\\ncontaining a newline\n'
    )
    assert entry.a == 'A value:\ncontaining a newline'


def test_ignore_private_as_tsv():
    entry = Entry()
    entry._zero = "to be removed"
    entry.one = "one value"
    entry._two = "should be removed"
    entry.two = "two value"
    entry._three = "three"

    assert entry.tsv == (
        'one\ttwo\n'
        'one value\ttwo value\n'
    )


def test_postaladdress_as_tsv():
    entry = Entry()
    entry.streetAddress = "Aviation House, 125 Kingsway"
    entry.addressLocality = "Holborn"
    entry.addressRegion = "London"
    entry.postcode = "WC2B 6NH"
    entry.addressCountry = "GB"

    data = entry.tsv
    assert data == (
        'addressCountry\taddressLocality\taddressRegion\tpostcode\tstreetAddress\n'  # NOQA
        'GB\tHolborn\tLondon\tWC2B 6NH\tAviation House, 125 Kingsway\n'              # NOQA
    )


def test_postaladdress_from_tsv():
    entry = Entry()
    entry.tsv = (
        'addressCountry\taddressLocality\taddressRegion\tpostcode\tstreetAddress\n'  # NOQA
        'GB\tHolborn\tLondon\tWC2B 6NH\tAviation House, 125 Kingsway\n'              # NOQA
    )

    assert entry.streetAddress == "Aviation House, 125 Kingsway"
    assert entry.addressLocality == "Holborn"
    assert entry.addressRegion == "London"
    assert entry.postcode == "WC2B 6NH"
    assert entry.addressCountry == "GB"
