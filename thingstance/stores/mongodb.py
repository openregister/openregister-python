import math
from ..store import Store
from ..thing import Thing
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class MongoStore(Store):

    """MongoDB storage for Things."""

    def __init__(self, mongo_uri, collection="things"):
        client = MongoClient(mongo_uri)
        self.db = client.get_default_database()
        self.things = self.db[collection]

    def put(self, thing):
        doc = thing.primitive
        doc['_id'] = thing.hash
        try:
            self.things.insert(doc)
        except DuplicateKeyError:
            pass

    def get(self, hash):
        doc = self.things.find_one({'_id': hash})
        if doc is None:
            return None

        del doc['_id']

        thing = Thing()
        thing.primitive = doc
        return thing

    def find(self, query={}, page=1, page_size=50,
             paginate_if_longer_than=10000):

        total = self.things.find(query).count()
        if total < paginate_if_longer_than:
            page_size = total
            pages = 0
        else:
            pages = math.ceil(total/page_size)
        if page == 1:
            start = page - 1
        else:
            start = (page - 1) * page_size

        cursor = self.things.find(query)[start: start+page_size]
        things = [Thing(**record) for record in cursor]

        meta = {
            "query": query,
            "total": total,
            "page":  page,
            "pages": pages,
        }

        return meta, things
