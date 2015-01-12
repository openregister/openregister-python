import pytest
from thingstance import Thing
from thingstance.stores.mongodb import MongoStore
from pymongo import Connection

database = 'testing_things'

Connection().drop_database(database)
store = MongoStore(database=database)


def test_not_found():
    thing = store.get('invalid hash')
    assert thing is None


def test_simple_store():
    text = 'This is a test'
    thing = Thing(text=text)
    store.put(thing)

    got = store.get(thing.hash)
    assert thing.hash == got.hash
    assert thing.text == got.text


def test_store():
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


def test_get_latest_by_name():
    with pytest.raises(NotImplementedError):
        store.get_latest(name="toves")


def test_own_database_and_collection():
    database = 'testing_named_things'
    collection = 'testing_collection'
    store = MongoStore(database=database, collection=collection)
    assert store.db.name == database
    assert store.things.name == collection


def test_own_db():
    database = 'testing_other_things'
    db = Connection()[database]
    store = MongoStore(db=db)
    assert store.db == db
    assert store.db.name == database


def test_idempotent_put():
    thing = Thing(text='Idempotent?')
    store.put(thing)
    store.put(thing)
    store.put(thing)
