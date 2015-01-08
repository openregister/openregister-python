from thingstance import Thing
from thingstance.store.memory import MemoryStore

store = MemoryStore()


def test_memory_store():
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
