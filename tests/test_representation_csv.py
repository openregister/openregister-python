from entry import Entry
from entry.representations.csv import content_type


def test_csv_content_type():
    assert content_type == "text/csv; charset=utf-8"


def test_empty_entry_as_csv():
    entry = Entry()
    data = entry.csv
    assert data == ''


def test_empty_entry_from_csv():
    entry = Entry()
    entry.csv = ('')
    assert entry.csv == ('')


def test_simple_as_csv():
    entry = Entry()
    entry.a = "A value"
    data = entry.csv
    assert data == (
        '"a"\r\n'
        '"A value"\r\n'
    )


def test_ignore_private_as_csv():
    entry = Entry()
    entry._zero = "to be removed"
    entry.one = "one value"
    entry._two = "should be removed"
    entry.two = "two value"
    entry._three = "three"

    data = entry.csv
    assert data == (
        '"one","two"\r\n'
        '"one value","two value"\r\n'
    )


def test_postaladdress_as_csv():
    entry = Entry()
    entry.streetAddress = "Aviation House, 125 Kingsway"
    entry.addressLocality = "Holborn"
    entry.addressRegion = "London"
    entry.postcode = "WC2B 6NH"
    entry.addressCountry = "GB"

    data = entry.csv
    assert data == (
        '"addressCountry","addressLocality","addressRegion","postcode","streetAddress"\r\n'  # NOQA
        '"GB","Holborn","London","WC2B 6NH","Aviation House, 125 Kingsway"\r\n'              # NOQA
    )


def test_postaladdress_from_csv():
    entry = Entry()
    entry.csv = (
        '"addressCountry","addressLocality","addressRegion","postcode","streetAddress"\r\n'  # NOQA
        '"GB","Holborn","London","WC2B 6NH","Aviation House, 125 Kingsway"\r\n'              # NOQA
    )

    assert entry.streetAddress == "Aviation House, 125 Kingsway"
    assert entry.addressLocality == "Holborn"
    assert entry.addressRegion == "London"
    assert entry.postcode == "WC2B 6NH"
    assert entry.addressCountry == "GB"


def test_trim_csv_headings():
    entry = Entry()
    entry.csv = (
        '"  addressCountry","addressLocality  "," addressRegion","postcode"," streetAddress"\r\n'  # NOQA
        '"GB","Holborn","London","WC2B 6NH","Aviation House, 125 Kingsway"\r\n'              # NOQA
    )

    assert entry.streetAddress == "Aviation House, 125 Kingsway"
    assert entry.addressLocality == "Holborn"
    assert entry.addressRegion == "London"
    assert entry.postcode == "WC2B 6NH"
    assert entry.addressCountry == "GB"
