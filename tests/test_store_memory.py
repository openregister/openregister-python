from thingstance import Thing
from thingstance.stores.memory import MemoryStore

store = MemoryStore()


def test_not_found():
    thing = store.get('invalid hash')
    assert thing is None


def test_simple_store():
    text = 'This is a test'
    thing = Thing(text=text)
    store.put(thing)

    got = store.get(thing.hash)
    assert thing.hash == got.hash
    assert thing.text == got.text


def test_store():
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


def test_get_latest_by_name():
    store.put(Thing(name="toves", text='Slithy'))
    store.put(Thing(name="borogoves", text='Mimsy'))

    thing = store.get_latest(name="toves")
    assert thing.name == "toves"
    assert thing.text == "Slithy"

    v1 = store.get_latest(name="borogoves")
    assert v1.name == "borogoves"
    assert v1.text == "Mimsy"

    v2 = Thing(name="borogoves", text='All mimsy')
    store.put(v2)

    thing = store.get_latest(name="borogoves")
    assert thing.hash == v2.hash
    assert thing.name == "borogoves"
    assert thing.text == "All mimsy"

    thing = store.get(v1.hash)
    assert thing.hash == v1.hash
    assert thing.name == "borogoves"
    assert thing.text == "Mimsy"
