from openregister.item import Item
from openregister.entry import Entry
from openregister.record import Record
from datetime import datetime


def test_new_empty_record():
    record = Record()
    assert record.entry is None
    assert record.item is None


def test_new_record():
    item = Item(school='1234', name='Example School')
    entry = Entry(1, item.hash)
    record = Record(entry, item)
    assert record.entry is entry
    assert record.item is item


def test_record_from_primitive():
    timestamp = datetime.utcnow().replace(microsecond=0)
    item_hash = '86919082e44f7256557646f4a764e2af92e53951'

    primitive = {
        'timestamp': timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
        'item-hash': item_hash,
        'entry-number': 99,
        'school': '123456',
        'name': 'School Name'
    }

    record = Record()
    record.primitive = primitive

    assert record.entry.timestamp == timestamp
    assert record.entry.item_hash == item_hash
    assert record.entry.entry_number == 99
    assert record.item.school == '123456'
    assert record.item.name == 'School Name'

    assert record.primitive == primitive
