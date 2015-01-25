import pytest
from thingstance import Thing
from thingstance.store import Store

store = Store()
thing = Thing()


def test_store_interface():
    with pytest.raises(NotImplementedError):
        store.put(thing)

    with pytest.raises(NotImplementedError):
        store.get(thing.hash)

    with pytest.raises(NotImplementedError):
        store.get_latest()

    with pytest.raises(NotImplementedError):
        store.find()
