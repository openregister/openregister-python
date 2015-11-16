from openregister import Item
from openregister.stores.memory import MemoryStore

store = MemoryStore()


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


def test_get_latest_by_name():
    store.put(Item(name="toves", text='Slithy'))
    store.put(Item(name="borogoves", text='Mimsy'))

    item = store.get_latest(name="toves")
    assert item.name == "toves"
    assert item.text == "Slithy"

    v1 = store.get_latest(name="borogoves")
    assert v1.name == "borogoves"
    assert v1.text == "Mimsy"

    v2 = Item(name="borogoves", text='All mimsy')
    store.put(v2)

    item = store.get_latest(name="borogoves")
    assert item.hash == v2.hash
    assert item.name == "borogoves"
    assert item.text == "All mimsy"

    item = store.get(v1.hash)
    assert item.hash == v1.hash
    assert item.name == "borogoves"
    assert item.text == "Mimsy"


def test_idempotent_put():
    item = Item(text='Idempotent?')
    store.put(item)
    store.put(item)
    store.put(item)
