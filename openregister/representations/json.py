from ..item import Item
from ..writer import Writer
import json


content_type = 'application/json'


def load(self, text):
    """Item from JSON representation."""
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
    def __init__(self, stream, start="[", sep=",", eol="", end="]"):
        self.stream = stream
        self.sep = sep
        self.eol = eol
        self.end = end
        self.stream.write(start)
        self.sol = ""

    def write(self, item):
        self.stream.write(self.sol + dump(item) + self.eol)
        self.sol = self.sep

    def close(self):
        self.stream.write(self.end)


Item.json = property(dump, load)
