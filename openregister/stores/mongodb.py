import math
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
        self.items = self.db[prefix + "items"]
        self.entries = self.db[prefix + "entries"]
        self.records = self.db[prefix + "records"]

        # self-incrementing entry_number
        self.entry_number = prefix + "entry_number"

    def put(self, item):
        doc = item.primitive
        doc['_id'] = item.hash
        try:
            self.items.insert(doc)
        except DuplicateKeyError:
            pass

    def get(self, hash):
        doc = self.items.find_one({'_id': hash})
        if doc is None:
            return None

        del doc['_id']

        item = Item()
        item.primitive = doc
        return item

    def find(self, query={}, page=1, page_size=None):
        if page_size is None or page_size < 0:
            page_size = self.page_size

        meta = {}
        meta['total'] = self.items.find(query).count()
        meta['pages'] = math.ceil(meta['total']/page_size)
        meta['page'] = page

        items = [Item(**doc) for doc in self.items.find()
                 .skip(page_size*(page-1))
                 .limit(page_size)]

        return meta, items

    #
    #  entries
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
        del doc['entry_number']

        self.entries.insert(doc)

        return entry
