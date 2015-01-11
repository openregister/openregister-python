import pytest
from thingstance import Thing
from thingstance.stores.mongodb import MongoStore

store = MongoStore()


def test_mongodb_store():
    thing = Thing()
    with pytest.raises(NotImplementedError):
        store.put(thing)


def test_mongodb_get_latest_by_name():
    with pytest.raises(NotImplementedError):
        store.get_latest(name="toves")
