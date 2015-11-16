from openregister import Item
from openregister.representations.csv import content_type


def test_csv_content_type():
    assert content_type == "text/csv; charset=utf-8"


def test_empty_item_as_csv():
    item = Item()
    data = item.csv
    assert data == ''


def test_empty_item_from_csv():
    item = Item()
    item.csv = ('')
    assert item.csv == ('')


def test_simple_as_csv():
    item = Item()
    item.a = "A value"
    data = item.csv
    assert data == (
        '"a"\r\n'
        '"A value"\r\n'
    )


def test_ignore_private_as_csv():
    item = Item()
    item._zero = "to be removed"
    item.one = "one value"
    item._two = "should be removed"
    item.two = "two value"
    item._three = "three"

    data = item.csv
    assert data == (
        '"one","two"\r\n'
        '"one value","two value"\r\n'
    )


def test_postaladdress_as_csv():
    item = Item()
    item.streetAddress = "Aviation House, 125 Kingsway"
    item.addressLocality = "Holborn"
    item.addressRegion = "London"
    item.postcode = "WC2B 6NH"
    item.addressCountry = "GB"

    data = item.csv
    assert data == (
        '"addressCountry","addressLocality","addressRegion","postcode","streetAddress"\r\n'  # NOQA
        '"GB","Holborn","London","WC2B 6NH","Aviation House, 125 Kingsway"\r\n'              # NOQA
    )


def test_postaladdress_from_csv():
    item = Item()
    item.csv = (
        '"addressCountry","addressLocality","addressRegion","postcode","streetAddress"\r\n'  # NOQA
        '"GB","Holborn","London","WC2B 6NH","Aviation House, 125 Kingsway"\r\n'              # NOQA
    )

    assert item.streetAddress == "Aviation House, 125 Kingsway"
    assert item.addressLocality == "Holborn"
    assert item.addressRegion == "London"
    assert item.postcode == "WC2B 6NH"
    assert item.addressCountry == "GB"


def test_trim_csv_headings():
    item = Item()
    item.csv = (
        '"  addressCountry","addressLocality  "," addressRegion","postcode"," streetAddress"\r\n'  # NOQA
        '"GB","Holborn","London","WC2B 6NH","Aviation House, 125 Kingsway"\r\n'              # NOQA
    )

    assert item.streetAddress == "Aviation House, 125 Kingsway"
    assert item.addressLocality == "Holborn"
    assert item.addressRegion == "London"
    assert item.postcode == "WC2B 6NH"
    assert item.addressCountry == "GB"
