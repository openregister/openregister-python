from ..entry import Entry
from ..writer import Writer
import json


content_type = 'application/json'


def load(self, text):
    """Entry from JSON representation."""
    self.__dict__ = json.loads(text)


def dump(self):
    """JSON representation."""
    return json.dumps(
        self.primitive,
        sort_keys=True,
        ensure_ascii=False,
        separators=(',', ':'))


class Writer(Writer):
    """Write JSON array."""
    def __init__(self, stream, start="[", sep=",", end="]"):
        self.stream = stream
        self.sep = sep
        self.end = end
        self.stream.write(start)
        self.sol = ""

    def write(self, entry):
        self.stream.write(self.sol + dump(entry))
        self.sol = self.sep

    def close(self):
        self.stream.write(self.end)


Entry.json = property(dump, load)
