import pytest
import os
from openregister import Item
from openregister.stores.mongodb import MongoStore

from pymongo import MongoClient
mongo_host = os.getenv('DB_PORT_27017_TCP_ADDR', '127.0.0.1')
mongo_uri = 'mongodb://%s:27017/openregister-python-test' % mongo_host
client = MongoClient(mongo_uri)

store = MongoStore(mongo_uri)


def clear_db(mongo_uri, db_name):
    client = MongoClient(mongo_uri)
    client.drop_database(db_name)


def test_not_found():
    item = store.get('invalid hash')
    assert item is None


def test_simple_store():
    text = 'This is a test'
    item = Item(text=text)
    store.put(item)

    got = store.get(item.hash)
    assert item.hash == got.hash
    assert item.text == got.text


def test_store():
    item = Item()
    empty_hash = item.hash
    store.put(item)

    item = Item(text='Foo Value')
    foo_hash = item.hash
    store.put(item)

    item = Item(text='Bar Value')
    bar_hash = item.hash
    store.put(item)

    item = store.get(empty_hash)
    assert item.hash == empty_hash

    item = store.get(foo_hash)
    assert item.hash == foo_hash
    assert item.text == 'Foo Value'

    item = store.get(bar_hash)
    assert item.hash == bar_hash
    assert item.text == 'Bar Value'


def test_tags():
    item = Item()
    item.tags = {'one', 'two', 'three'}
    item = store.put(item)


def test_get_latest_by_name():
    with pytest.raises(NotImplementedError):
        store.get_latest(name="toves")


def test_own_database_and_collection():
    mongo_uri = 'mongodb://%s:27017/testing_named_entries' % mongo_host
    collection = 'testing_collection'
    store = MongoStore(mongo_uri, collection=collection)
    assert store.db.name == 'testing_named_entries'
    assert store.entries.name == collection
    clear_db(mongo_uri, store.db.name)


def test_own_db():
    mongo_uri = 'mongodb://%s:27017/testing_other_entries' % mongo_host
    store = MongoStore(mongo_uri)
    assert store.db.name == 'testing_other_entries'
    clear_db(mongo_uri, store.db.name)


def test_idempotent_put():
    item = Item(text='Idempotent?')
    store.put(item)
    store.put(item)
    store.put(item)


def test_find():
    mongo_uri = 'mongodb://%s:27017/testing_finding' % mongo_host
    store = MongoStore(mongo_uri)
    store.put(Item(name='one', tags={'tag1'}))
    store.put(Item(name='two', tags={'tag2'}))
    store.put(Item(name='three', tags={}))
    store.put(Item(name='four', tags={'tag2'}))

    meta, entries = store.find()
    assert meta['total'] == 4
    assert meta['page'] == 1
    assert meta['pages'] == 1
    assert len(entries) == 4

    meta, entries = store.find(page_size=2, paginate_if_longer_than=2)
    assert meta['page'] == 1
    assert meta['pages'] == 2
    assert len(entries) == 2

    meta, entries = store.find(page=2, page_size=2, paginate_if_longer_than=2)
    assert meta['page'] == 2
    assert meta['pages'] == 2
    assert len(entries) == 2

    clear_db(mongo_uri, store.db.name)
