import pytest
import os
from entry import Entry
from entry.stores.mongodb import MongoStore

from pymongo import MongoClient
mongo_host = os.getenv('DB_PORT_27017_TCP_ADDR', '127.0.0.1')
mongo_uri = 'mongodb://%s:27017/openregister' % mongo_host
client = MongoClient(mongo_uri)

store = MongoStore(mongo_uri)


def clear_db(mongo_uri, db_name):
    client = MongoClient(mongo_uri)
    client.drop_database(db_name)


def test_not_found():
    entry = store.get('invalid hash')
    assert entry is None


def test_simple_store():
    text = 'This is a test'
    entry = Entry(text=text)
    store.put(entry)

    got = store.get(entry.hash)
    assert entry.hash == got.hash
    assert entry.text == got.text


def test_store():
    entry = Entry()
    empty_hash = entry.hash
    store.put(entry)

    entry = Entry(text='Foo Value')
    foo_hash = entry.hash
    store.put(entry)

    entry = Entry(text='Bar Value')
    bar_hash = entry.hash
    store.put(entry)

    entry = store.get(empty_hash)
    assert entry.hash == empty_hash

    entry = store.get(foo_hash)
    assert entry.hash == foo_hash
    assert entry.text == 'Foo Value'

    entry = store.get(bar_hash)
    assert entry.hash == bar_hash
    assert entry.text == 'Bar Value'


def test_tags():
    entry = Entry()
    entry.tags = {'one', 'two', 'three'}
    entry = store.put(entry)


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
    entry = Entry(text='Idempotent?')
    store.put(entry)
    store.put(entry)
    store.put(entry)


def test_find():
    mongo_uri = 'mongodb://%s:27017/testing_finding' % mongo_host
    store = MongoStore(mongo_uri)
    store.put(Entry(name='one', tags={'tag1'}))
    store.put(Entry(name='two', tags={'tag2'}))
    store.put(Entry(name='three', tags={}))
    store.put(Entry(name='four', tags={'tag2'}))

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
