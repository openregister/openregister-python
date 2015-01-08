from thingstance import Thing
from thingstance.store.memory import MemoryStore

store = MemoryStore()


def test_memory_store():
    emptyThing = Thing()
    hash = emptyThing.hash

    store.put(emptyThing)

    thing = store.get(hash)

    assert thing.hash == hash
