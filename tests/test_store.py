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
        store.get(item.hash)

    with pytest.raises(NotImplementedError):
        store.find()

    with pytest.raises(NotImplementedError):
        store.add(item)
