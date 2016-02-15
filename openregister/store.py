class Store(object):

    """Interface for storage of Items."""
    def __init__(self, register="unknown"):
        pass

    def put(self, item):
        """Store item"""
        raise NotImplementedError

    def get(self, hash):
        """Retrieve item"""
        raise NotImplementedError

    def find(self, query={}, page=1, page_size=50):
        raise NotImplementedError

    def find_all(self, query={}):
        raise NotImplementedError

    def add(self, item, timestamp=None):
        """Add item as a new entry"""
        raise NotImplementedError
