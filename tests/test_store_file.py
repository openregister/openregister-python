import pytest
from tempdir import TempDir
from openregister import Item
from openregister.stores.file import FileStore


def test_not_found():
    store = FileStore()
    item = store.get('invalid hash')
    assert item is None


def test_simple_store():
    with TempDir() as tmp:
        store = FileStore(dir=tmp)
        text = 'This is a test'
        item = Item(text=text)
        store.put(item)

        got = store.get(item.hash)
        assert item.hash == got.hash
        assert item.text == got.text


def test_store():
    with TempDir() as tmp:
        store = FileStore(dir=tmp)

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
    with TempDir() as tmp:
        store = FileStore(dir=tmp)
        item = Item()
        item.tags = {'one', 'two', 'three'}
        item = store.put(item)


def test_get_latest_by_name():
    with TempDir() as tmp:
        store = FileStore(dir=tmp)
        with pytest.raises(NotImplementedError):
            store.get_latest(name="toves")


def test_own_dir_and_suffix():
    dir = './tmp/testing_named_entries'
    suffix = ''
    store = FileStore(dir=dir, suffix=suffix)
    assert store.dir == dir
    assert store.suffix == suffix


def test_idempotent_put():
    with TempDir() as tmp:
        store = FileStore(dir=tmp)
        item = Item(text='Idempotent?')
        store.put(item)
        store.put(item)
        store.put(item)
