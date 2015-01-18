import os.path
from ..store import Store
from ..thing import Thing


class FileStore(Store):

    """Store Things as flat-files."""

    def __init__(self, dir="./things", suffix=".json"):
        self.dir = dir
        self.suffix = suffix

    def path(self, hash):
        return os.path.join(self.dir, hash + self.suffix)

    def put(self, thing):
        with open(self.path(thing.hash), 'w') as file:
            file.write(thing.json)

    def get(self, hash):
        thing = Thing()
        try:
            with open(self.path(hash), 'r') as file:
                thing.json = file.read()
            return thing
        except FileNotFoundError:
            return None


store = FileStore()
