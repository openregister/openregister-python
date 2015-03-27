import pytest
from tempdir import TempDir
from entry import Entry
from entry.stores.file import FileStore


def test_not_found():
    store = FileStore()
    entry = store.get('invalid hash')
    assert entry is None


def test_simple_store():
    with TempDir() as tmp:
        store = FileStore(dir=tmp)
        text = 'This is a test'
        entry = Entry(text=text)
        store.put(entry)

        got = store.get(entry.hash)
        assert entry.hash == got.hash
        assert entry.text == got.text


def test_store():
    with TempDir() as tmp:
        store = FileStore(dir=tmp)

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
    with TempDir() as tmp:
        store = FileStore(dir=tmp)
        entry = Entry()
        entry.tags = {'one', 'two', 'three'}
        entry = store.put(entry)


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
        entry = Entry(text='Idempotent?')
        store.put(entry)
        store.put(entry)
        store.put(entry)
