import math
from ..store import Store
from ..item import Item
from ..entry import Entry
from pymongo import MongoClient, ReturnDocument
from pymongo.errors import DuplicateKeyError


class MongoStore(Store):

    """MongoDB storage for Items."""

    def __init__(self, mongo_uri, prefix=""):
        client = MongoClient(mongo_uri)
        self.db = client.get_default_database()

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

    def find(self, query={}, page=1, page_size=50,
             paginate_if_longer_than=10000):

        total = self.items.find(query).count()
        if total < paginate_if_longer_than:
            page_size = total
            pages = 1
        else:
            pages = math.ceil(total/page_size)
        if page == 1:
            start = page - 1
        else:
            start = (page - 1) * page_size

        cursor = self.items.find(query)[start: start+page_size]
        items = [Item(**record) for record in cursor]

        meta = {
            "query": query,
            "total": total,
            "page":  page,
            "pages": pages,
        }

        return meta, items

    def find_all(self, query):
        cursor = self.items.find(query)
        items = [Item(**record) for record in cursor]
        return items

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
