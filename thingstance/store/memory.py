class MemoryStore(object):

    """Simple in-memory storage for Things."""

    things = {}

    def get(self, hash):
        return self.things[hash]

    def put(self, thing):
        hash = thing.hash
        self.things[hash] = thing

store = MemoryStore()
