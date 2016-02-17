import os.path
from ..store import Store
from ..item import Item


class FileStore(Store):

    """Store Items as flat-files."""

    def __init__(self, register="", dir="./data", suffix=".json"):
        self.dir = dir
        self.suffix = suffix

    def path(self, hash):
        return os.path.join(self.dir, hash + self.suffix)

    def put(self, item):
        with open(self.path(item.hash), 'w') as file:
            file.write(item.json)

    def item(self, hash):
        item = Item()
        try:
            with open(self.path(hash), 'r') as file:
                item.json = file.read()
            return item
        except FileNotFoundError:
            return None


store = FileStore()
