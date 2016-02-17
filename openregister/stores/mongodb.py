from ..store import Store
from ..item import Item
from ..entry import Entry
from pymongo import MongoClient, ReturnDocument
from pymongo.errors import DuplicateKeyError


class MongoStore(Store):

    """MongoDB storage for Items."""

    def __init__(self, mongo_uri, prefix="", page_size=None):
        client = MongoClient(mongo_uri)
        self.db = client.get_default_database()

        if page_size is not None:
            self.page_size = page_size

        # allows multiple registers in a single database
        self.prefix = prefix

        # mongo collections
        self._items = self.db[prefix + "items"]
        self._entries = self.db[prefix + "entries"]
        self._records = self.db[prefix + "records"]

        # self-incrementing entry_number
        self.entry_number = prefix + "entry_number"

    #
    #  item
    #
    def put(self, item):
        doc = item.primitive
        doc['_id'] = item.hash
        try:
            self._items.insert(doc)
        except DuplicateKeyError:
            pass
        return item

    def item(self, item_hash):
        doc = self._items.find_one({'_id': item_hash})
        if doc is None:
            return None

        del doc['_id']

        item = Item()
        item.primitive = doc
        return item

    #
    #  entry
    #
    def next_entry_number(self):
        return self.db.counters.find_one_and_update(
            {'_id': self.entry_number},
            {'$inc': {'seq': 1}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )['seq']

    def add(self, item, timestamp=None):
        self.put(item)

        entry = Entry(self.next_entry_number(), item.hash, timestamp)

        doc = entry.primitive
        doc['_id'] = entry.entry_number
        del doc['entry-number']

        self._entries.insert(doc)

        return entry

    #
    #  collections
    #
    def _query(self, query={}):
        for key in query:
            if query[key] is None or query[key] == '':
                del query['key']

    def items(self, item_hash=None, page=1, page_size=None):
        collection = self._items
        query = self._query({'item-hash': {'$gt': item_hash}})
        meta = self.meta(collection.find(query).count(), page, page_size)

        items = [Item(**doc) for doc in collection.find(query)
                 .skip(meta['skip'])
                 .limit(meta['page_size'])]

        return meta, items

    def entries(self, item_hash=None, page=1, page_size=None):
        collection = self._entries
        query = self._query({'item-hash': item_hash})
        meta = self.meta(collection.find(query).count(), page, page_size)

        entries = [Entry().primitive(doc) for doc in collection.find(query)
                   .skip(meta['skip'])
                   .limit(meta['page_size'])]

        return meta, entries
