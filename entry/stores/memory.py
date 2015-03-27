from ..store import Store


class MemoryStore(Store):

    """Simple in-memory storage for Entries."""

    entries = {}
    latest = {}

    def put(self, entry):
        hash = entry.hash
        self.entries[hash] = entry

        try:
            self.latest[entry.name] = entry
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
