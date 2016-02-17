from openregister import Item
from openregister.stores.memory import MemoryStore

store = MemoryStore()


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


def test_idempotent_put():
    item = Item(text='Idempotent?')
    store.put(item)
    store.put(item)
    store.put(item)
