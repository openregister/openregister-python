from entry import Entry
from entry.stores.memory import MemoryStore

store = MemoryStore()


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


def test_get_latest_by_name():
    store.put(Entry(name="toves", text='Slithy'))
    store.put(Entry(name="borogoves", text='Mimsy'))

    entry = store.get_latest(name="toves")
    assert entry.name == "toves"
    assert entry.text == "Slithy"

    v1 = store.get_latest(name="borogoves")
    assert v1.name == "borogoves"
    assert v1.text == "Mimsy"

    v2 = Entry(name="borogoves", text='All mimsy')
    store.put(v2)

    entry = store.get_latest(name="borogoves")
    assert entry.hash == v2.hash
    assert entry.name == "borogoves"
    assert entry.text == "All mimsy"

    entry = store.get(v1.hash)
    assert entry.hash == v1.hash
    assert entry.name == "borogoves"
    assert entry.text == "Mimsy"


def test_idempotent_put():
    entry = Entry(text='Idempotent?')
    store.put(entry)
    store.put(entry)
    store.put(entry)
