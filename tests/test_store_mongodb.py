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
    item = store.item('invalid hash')
    assert item is None


def test_simple_store():
    text = 'This is a test'
    item = Item(text=text)
    store.put(item)

    got = store.item(item.hash)
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

    item = store.item(empty_hash)
    assert item.hash == empty_hash

    item = store.item(foo_hash)
    assert item.hash == foo_hash
    assert item.text == 'Foo Value'

    item = store.item(bar_hash)
    assert item.hash == bar_hash
    assert item.text == 'Bar Value'


def test_tags():
    item = Item()
    item.tags = {'one', 'two', 'three'}
    item = store.put(item)


def test_own_database_and_prefix():
    mongo_uri = 'mongodb://%s:27017/testing_named_items' % mongo_host
    prefix = 'testing_'
    store = MongoStore(mongo_uri, prefix=prefix)
    assert store.db.name == 'testing_named_items'
    assert store._items.name == prefix + "items"
    assert store._entries.name == prefix + "entries"
    clear_db(mongo_uri, store.db.name)


def test_own_db():
    mongo_uri = 'mongodb://%s:27017/testing_other_items' % mongo_host
    store = MongoStore(mongo_uri)
    assert store.db.name == 'testing_other_items'
    clear_db(mongo_uri, store.db.name)


def test_idempotent_put():
    item = Item(text='Idempotent?')
    store.put(item)
    store.put(item)
    store.put(item)


def test_add():
    clear_db(mongo_uri, store.db.name)
    store.add(Item(n='1'))
    store.add(Item(n='2'))
    store.add(Item(n='3'))
    store.add(Item(n='4'))
    clear_db(mongo_uri, store.db.name)


def test_items():
    mongo_uri = 'mongodb://%s:27017/testing_finding' % mongo_host
    store = MongoStore(mongo_uri)
    clear_db(mongo_uri, store.db.name)
    store.put(Item(name='one', tags={'tag1'}))
    store.put(Item(name='two', tags={'tag1'}))
    store.put(Item(name='three', tags={'tag1'}))
    store.put(Item(name='four', tags={'tag2'}))
    store.put(Item(name='five', tags={'tag2'}))
    store.put(Item(name='six', tags={'tag1'}))
    store.put(Item(name='seven', tags={'tag2'}))
    store.put(Item(name='eight', tags={'tag2'}))
    store.put(Item(name='nine', tags={'tag1'}))
    store.put(Item(name='ten', tags={'tag1'}))

    meta, items = store.items()
    assert meta['total'] == 10
    assert meta['page'] == 1
    assert meta['pages'] == 1
    assert len(items) == 10

    meta, items = store.items(page_size=8)
    assert meta['page'] == 1
    assert meta['pages'] == 2
    assert len(items) == 8

    meta, items = store.items(page=2, page_size=2)
    assert meta['page'] == 2
    assert meta['pages'] == 5
    assert len(items) == 2

    clear_db(mongo_uri, store.db.name)


def test_counting():
    clear_db(mongo_uri, store.db.name)
    store.put(Item(text='one'))
