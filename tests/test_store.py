import pytest
from openregister import Item
from openregister.store import Store

store = Store()
item = Item()


def test_store_interface():
    with pytest.raises(NotImplementedError):
        store.put(item)

    with pytest.raises(NotImplementedError):
        store.get(item.hash)

    with pytest.raises(NotImplementedError):
        store.get_latest()

    with pytest.raises(NotImplementedError):
        store.find()
