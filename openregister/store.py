class Store(object):

    """Interface for storage of Items."""
    def __init__(self, register="unknown"):
        pass

    def put(self, item):
        raise NotImplementedError

    def get(self, hash):
        raise NotImplementedError

    def get_latest(self, name=None):
        raise NotImplementedError

    def find(self, query={}, page=1, page_size=50):
        raise NotImplementedError

    def find_all(self, query={}):
        raise NotImplementedError
