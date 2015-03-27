import pytest
from entry import Entry
from entry.store import Store

store = Store()
entry = Entry()


def test_store_interface():
    with pytest.raises(NotImplementedError):
        store.put(entry)

    with pytest.raises(NotImplementedError):
        store.get(entry.hash)

    with pytest.raises(NotImplementedError):
        store.get_latest()

    with pytest.raises(NotImplementedError):
        store.find()
