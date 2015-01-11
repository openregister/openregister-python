from ..store import Store


class MemoryStore(Store):

    """Simple in-memory storage for Things."""

    things = {}
    latest = {}

    def put(self, thing):
        hash = thing.hash
        self.things[hash] = thing

        try:
            self.latest[thing.name] = thing
        except AttributeError:
            pass

    def get(self, hash):
        return self.things[hash]

    def get_latest(self, name=None):
        return self.latest[name]

store = MemoryStore()
