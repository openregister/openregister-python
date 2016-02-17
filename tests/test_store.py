import pytest
import numbers
from openregister import Item
from openregister.store import Store

store = Store()
item = Item()


def test_store_interface():
    assert isinstance(store.page_size, numbers.Integral)

    with pytest.raises(NotImplementedError):
        store.put(item)

    with pytest.raises(NotImplementedError):
        store.add(item)

    with pytest.raises(NotImplementedError):
        store.item(item.hash)

    with pytest.raises(NotImplementedError):
        store.items()

    with pytest.raises(NotImplementedError):
        store.entry(1)

    with pytest.raises(NotImplementedError):
        store.entries()

    with pytest.raises(NotImplementedError):
        store.record('foo')

    with pytest.raises(NotImplementedError):
        store.records()

    with pytest.raises(NotImplementedError):
        store.register('register')
