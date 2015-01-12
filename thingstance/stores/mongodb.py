from ..store import Store
from ..thing import Thing
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class MongoStore(Store):

    """MongoDB storage for Things."""

    def __init__(self, db=None,
                 database="thingstance",
                 collection="things"):
        if not db:
            client = MongoClient()
            db = client[database]
        self.db = db
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

store = MongoStore()
