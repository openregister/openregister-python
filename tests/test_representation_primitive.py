from entry import Entry


def test_empty_entry_as_primitive():
    entry = Entry()
    data = entry.primitive
    assert data == {}


def test_empty_entry_from_primitive():
    entry = Entry()
    entry.primitive = {}
    assert entry.primitive == {}


def test_ignore_private_as_primitive():
    entry = Entry()
    entry._zero = "to be removed"
    entry.one = "one value"
    entry._two = "should be removed"
    entry.two = "two value"
    entry._three = "three"

    data = entry.primitive
    assert data == ({"one": "one value", "two": "two value"})


def test_postaladdress_as_primitive():
    entry = Entry()
    entry.streetAddress = "Aviation House, 125 Kingsway"
    entry.addressLocality = "Holborn"
    entry.addressRegion = "London"
    entry.postcode = "WC2B 6NH"
    entry.addressCountry = "GB"

    assert entry.primitive == {
        'addressCountry': 'GB',
        'addressLocality': 'Holborn',
        'addressRegion': 'London',
        'postcode': 'WC2B 6NH',
        'streetAddress': 'Aviation House, 125 Kingsway'}


def test_postaladdress_from_primitive():
    entry = Entry()
    entry.primitive = {
        'addressCountry': 'GB',
        'addressLocality': 'Holborn',
        'addressRegion': 'London',
        'postcode': 'WC2B 6NH',
        'streetAddress': 'Aviation House, 125 Kingsway'}

    assert entry.streetAddress == "Aviation House, 125 Kingsway"
    assert entry.addressLocality == "Holborn"
    assert entry.addressRegion == "London"
    assert entry.postcode == "WC2B 6NH"
    assert entry.addressCountry == "GB"


def test_set_of_tags_as_primitive():
    entry = Entry(name='foo', fields={'z', 'b', 'c', 'z'})
    assert entry.primitive == {
        'fields': ['b', 'c', 'z'],
        'name': 'foo'}


def test_set_of_tags_from_primitive():
    entry = Entry()
    entry.primitive = {
        'fields': ['a', 'b', 'c'],
        'name': 'foo'}
    assert entry.name == 'foo'
    assert entry.fields == ['a', 'b', 'c']
