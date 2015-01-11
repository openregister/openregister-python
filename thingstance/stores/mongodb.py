from ..store import Store


class MongoStore(Store):

    """MongoDB storage for Things."""


store = MongoStore()
