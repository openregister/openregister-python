class Store(object):

    """Interface for storage of Entries."""

    def put(self, entry):
        raise NotImplementedError

    def get(self, hash):
        raise NotImplementedError

    def get_latest(self, name=None):
        raise NotImplementedError

    def find(self, query={}, page=1, page_size=50):
        raise NotImplementedError
