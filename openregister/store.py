import math


class Store(object):

    page_size = 10000

    """Interface for storage of Items."""
    def __init__(self):
        pass

    def meta(self, total, page=1, page_size=None):
        """
        Calculate statistics for a collection
        return: meta
        """
        if page_size is None or page_size < 0:
            page_size = self.page_size

        meta = {}
        meta['total'] = total
        meta['page_size'] = page_size
        meta['pages'] = math.ceil(meta['total']/page_size)
        meta['page'] = page
        meta['skip'] = page_size * (page-1)
        return meta

    def put(self, item):
        """
        Store item
        returns: item
        """
        raise NotImplementedError

    def add(self, item, timestamp=None):
        """
        Add item as a new entry
        returns: entry
        """
        raise NotImplementedError

    def item(self, item_hash):
        """
        Retrieve item
        returns: item
        """
        raise NotImplementedError

    def items(self, item_hash=None, page=1, page_size=None):
        """
        Retrieve collection of items
        item_hash: starting at this item
        returns: item[]
        """
        raise NotImplementedError

    def entry(self, entry_number):
        """
        Retrieve an entry
        returns: entry
        """
        raise NotImplementedError

    def entries(self, item_hash=None, page=1, page_size=None):
        """
        Retrieve collection of entries
        item_hash: return only entries with this item_hash
        returns: entry[]
        """
        raise NotImplementedError

    def record(self, value):
        """
        Retrieve a record by key-field value
        returns: record
        """
        raise NotImplementedError

    def records(self, field=None, value=None, page=1, page_size=None):
        """
        Retrieve a records by field value
        returns: record[]
        """
        raise NotImplementedError

    def register(self, register_name):
        """
        Retrieve register info
        returns: register
        """
        raise NotImplementedError
