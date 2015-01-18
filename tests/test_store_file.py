import pytest
from tempdir import TempDir
from thingstance import Thing
from thingstance.stores.file import FileStore


def test_not_found():
    store = FileStore()
    thing = store.get('invalid hash')
    assert thing is None


def test_simple_store():
    with TempDir() as tmp:
        store = FileStore(dir=tmp)
        text = 'This is a test'
        thing = Thing(text=text)
        store.put(thing)

        got = store.get(thing.hash)
        assert thing.hash == got.hash
        assert thing.text == got.text


def test_store():
    with TempDir() as tmp:
        store = FileStore(dir=tmp)

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
    with TempDir() as tmp:
        store = FileStore(dir=tmp)
        thing = Thing()
        thing.tags = {'one', 'two', 'three'}
        thing = store.put(thing)


def test_get_latest_by_name():
    with TempDir() as tmp:
        store = FileStore(dir=tmp)
        with pytest.raises(NotImplementedError):
            store.get_latest(name="toves")


def test_own_dir_and_suffix():
    dir = './tmp/testing_named_things'
    suffix = ''
    store = FileStore(dir=dir, suffix=suffix)
    assert store.dir == dir
    assert store.suffix == suffix


def test_idempotent_put():
    with TempDir() as tmp:
        store = FileStore(dir=tmp)
        thing = Thing(text='Idempotent?')
        store.put(thing)
        store.put(thing)
        store.put(thing)
