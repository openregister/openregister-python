import os.path
from ..store import Store
from ..entry import Entry


class FileStore(Store):

    """Store Entries as flat-files."""

    def __init__(self, dir="./entries", suffix=".json"):
        self.dir = dir
        self.suffix = suffix

    def path(self, hash):
        return os.path.join(self.dir, hash + self.suffix)

    def put(self, entry):
        with open(self.path(entry.hash), 'w') as file:
            file.write(entry.json)

    def get(self, hash):
        entry = Entry()
        try:
            with open(self.path(hash), 'r') as file:
                entry.json = file.read()
            return entry
        except FileNotFoundError:
            return None


store = FileStore()
