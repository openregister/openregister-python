import pytest
from thingstance import Thing
from thingstance.stores.mongodb import MongoStore

store = MongoStore()


def test_memory_store():
    thing = Thing(text='Foo Value')
    foo_hash = thing.hash
    store.put(thing)

    thing = store.get(foo_hash)
    assert thing.hash == foo_hash
    assert thing.text == 'Foo Value'


def test_mongodb_get_latest_by_name():
    with pytest.raises(NotImplementedError):
        store.get_latest(name="toves")
