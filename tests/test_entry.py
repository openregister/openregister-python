import pytest
from datetime import datetime
from openregister.entry import Entry


def test_new_empty_entry():
    entry = Entry()
    assert entry.entry_number is None
    assert entry.item_hash is None
    assert entry.item_hash is None

    assert type(entry.timestamp) is datetime

    with pytest.raises(AttributeError):
        entry.zog


def test_new_entry_from_params():
    entry_number = 12345678901234567890123456789012345678901234567890
    timestamp = '2016-02-15T09:30:33Z'
    item_hash = '86919082e44f7256557646f4a764e2af92e53951'
    entry = Entry(entry_number, item_hash, timestamp)
    assert entry.entry_number == entry_number
    assert entry.item_hash == item_hash
    assert entry.timestamp == timestamp

    entry = Entry(item_hash=item_hash)
    assert entry.entry_number is None
    assert entry.item_hash == item_hash


def test_entry_as_primitive():
    timestamp = '2016-02-15T09:30:33Z'
    entry = Entry(timestamp=timestamp)
    assert entry.primitive == {'timestamp': timestamp}
    entry.entry_number = 99
    assert entry.primitive == {
        'timestamp': timestamp,
        'entry-number': 99
    }

    entry.item_hash = '86919082e44f7256557646f4a764e2af92e53951'
    assert entry.primitive == {
        'timestamp': timestamp,
        'item-hash': '86919082e44f7256557646f4a764e2af92e53951',
        'entry-number': 99
    }


def test_entry_from_primitive():
    entry = Entry()

    timestamp = datetime.utcnow().replace(microsecond=0)

    primitive = {
        'timestamp': timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
        'item-hash': '86919082e44f7256557646f4a764e2af92e53951',
        'entry-number': 99
    }

    entry.primitive = primitive
    assert entry.timestamp == timestamp
    assert entry.item_hash == primitive['item-hash']
    assert entry.entry_number == primitive['entry-number']
