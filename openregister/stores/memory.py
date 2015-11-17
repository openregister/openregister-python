from ..store import Store


class MemoryStore(Store):

    """Simple in-memory storage for Items."""

    entries = {}
    latest = {}

    def put(self, item):
        hash = item.hash
        self.entries[hash] = item

        try:
            self.latest[item.name] = item
        except AttributeError:
            pass

    def get(self, hash):
        try:
            return self.entries[hash]
        except KeyError:
            return None

    def get_latest(self, name=None):
        return self.latest[name]

store = MemoryStore()
