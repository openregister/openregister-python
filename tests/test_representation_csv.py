from thingstance import Thing
from thingstance.representations.csv import content_type


def test_csv_content_type():
    assert content_type == "text/csv; charset=utf-8"


def test_empty_thing_as_csv():
    thing = Thing()
    data = thing.csv
    assert data == '\r\n\r\n'


def test_empty_thing_from_csv():
    thing = Thing()
    thing.csv = ('')
    assert thing.csv == ('\r\n\r\n')


def test_simple_as_csv():
    thing = Thing()
    thing.a = "A value"
    data = thing.csv
    assert data == (
        '"a"\r\n'
        '"A value"\r\n'
    )


def test_ignore_private_as_csv():
    thing = Thing()
    thing._zero = "to be removed"
    thing.one = "one value"
    thing._two = "should be removed"
    thing.two = "two value"
    thing._three = "three"

    data = thing.csv
    assert data == (
        '"one","two"\r\n'
        '"one value","two value"\r\n'
    )


def test_postaladdress_as_csv():
    thing = Thing()
    thing.streetAddress = "Aviation House, 125 Kingsway"
    thing.addressLocality = "Holborn"
    thing.addressRegion = "London"
    thing.postcode = "WC2B 6NH"
    thing.addressCountry = "GB"

    data = thing.csv
    assert data == (
        '"addressCountry","addressLocality","addressRegion","postcode","streetAddress"\r\n'  # NOQA
        '"GB","Holborn","London","WC2B 6NH","Aviation House, 125 Kingsway"\r\n'              # NOQA
    )


def test_postaladdress_from_csv():
    thing = Thing()
    thing.csv = (
        '"addressCountry","addressLocality","addressRegion","postcode","streetAddress"\r\n'  # NOQA
        '"GB","Holborn","London","WC2B 6NH","Aviation House, 125 Kingsway"\r\n'              # NOQA
    )

    assert thing.streetAddress == "Aviation House, 125 Kingsway"
    assert thing.addressLocality == "Holborn"
    assert thing.addressRegion == "London"
    assert thing.postcode == "WC2B 6NH"
    assert thing.addressCountry == "GB"
