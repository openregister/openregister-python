import pytest
from thingstance import Thing
from thingstance.stores.mongodb import MongoStore
from pymongo import Connection

database = 'testing_things'

Connection().drop_database(database)
store = MongoStore(database=database)


def test_memory_store():
    thing = Thing()
    empty_hash = thing.hash
    store.put(thing)

    thing = Thing(text='Foo Value')
    foo_hash = thing.hash
    store.put(thing)

    thing = Thing(text='Bar Value')
    bar_hash = thing.hash
    store.put(thing)

    thing = store.get(empty_hash)
    assert thing.hash == empty_hash

    thing = store.get(foo_hash)
    assert thing.hash == foo_hash
    assert thing.text == 'Foo Value'

    thing = store.get(bar_hash)
    assert thing.hash == bar_hash
    assert thing.text == 'Bar Value'


def test_mongodb_get_latest_by_name():
    with pytest.raises(NotImplementedError):
        store.get_latest(name="toves")
