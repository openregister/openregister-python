from ..store import Store


class MemoryStore(Store):

    """Simple in-memory storage for Items."""

    items = {}
    latest = {}

    def put(self, item):
        hash = item.hash
        self.items[hash] = item

        try:
            self.latest[item.name] = item
        except AttributeError:
            pass

    def item(self, hash):
        try:
            return self.items[hash]
        except KeyError:
            return None

store = MemoryStore()
