from openregister.entry import Entry
from openregister.record import Record


def test_new_empty_record():
    entry = Entry()
    record = Record('country', 'ZZ', entry)
    assert record.field == 'country'
    assert record.value == 'ZZ'
    assert record.item is None
