import pytest
import os
from thingstance import Thing
from thingstance.stores.mongodb import MongoStore

from pymongo import MongoClient
mongo_host = os.getenv('DB_PORT_27017_TCP_ADDR', '127.0.0.1')
mongo_uri = 'mongodb://%s:27017/thingstance' % mongo_host
client = MongoClient(mongo_uri)

store = MongoStore(mongo_uri)


def clear_db(mongo_uri, db_name):
    client = MongoClient(mongo_uri)
    client.drop_database(db_name)


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


def test_tags():
    thing = Thing()
    thing.tags = {'one', 'two', 'three'}
    thing = store.put(thing)


def test_get_latest_by_name():
    with pytest.raises(NotImplementedError):
        store.get_latest(name="toves")


def test_own_database_and_collection():
    mongo_uri = 'mongodb://%s:27017/testing_named_things' % mongo_host
    collection = 'testing_collection'
    store = MongoStore(mongo_uri, collection=collection)
    assert store.db.name == 'testing_named_things'
    assert store.things.name == collection
    clear_db(mongo_uri, store.db.name)


def test_own_db():
    mongo_uri = 'mongodb://%s:27017/testing_other_things' % mongo_host
    store = MongoStore(mongo_uri)
    assert store.db.name == 'testing_other_things'
    clear_db(mongo_uri, store.db.name)


def test_idempotent_put():
    thing = Thing(text='Idempotent?')
    store.put(thing)
    store.put(thing)
    store.put(thing)


def test_find():
    mongo_uri = 'mongodb://%s:27017/testing_finding' % mongo_host
    store = MongoStore(mongo_uri)
    store.put(Thing(name='one', tags={'tag1'}))
    store.put(Thing(name='two', tags={'tag2'}))
    store.put(Thing(name='three', tags={}))
    store.put(Thing(name='four', tags={'tag2'}))

    meta, things = store.find()
    assert meta['total'] == 4
    assert meta['page'] == 1
    assert meta['pages'] == 1
    assert len(things) == 4

    meta, things = store.find(page_size=2, paginate_if_longer_than=2)
    assert meta['page'] == 1
    assert meta['pages'] == 2
    assert len(things) == 2

    meta, things = store.find(page=2, page_size=2, paginate_if_longer_than=2)
    assert meta['page'] == 2
    assert meta['pages'] == 2
    assert len(things) == 2

    clear_db(mongo_uri, store.db.name)
