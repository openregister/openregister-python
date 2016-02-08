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

    def get(self, hash):
        try:
            return self.items[hash]
        except KeyError:
            return None

    def get_latest(self, name=None):
        return self.latest[name]

store = MemoryStore()
