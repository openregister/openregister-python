from ..item import Item
from ..writer import Writer
import json
import re

START = re.compile('[ \t\n\r\[]*', re.VERBOSE | re.MULTILINE | re.DOTALL)
END = re.compile('[ \t\n\r,\]]*', re.VERBOSE | re.MULTILINE | re.DOTALL)

content_type = 'application/json'


def load(self, text):
    """Item from a JSON representation."""
    self.__dict__ = json.loads(text)


def dump(self):
    """Item as a JSON representation."""
    return json.dumps(
        self.primitive,
        sort_keys=True,
        ensure_ascii=False,
        separators=(',', ':'))


def reader(stream):
    """Read Items from a stream containing a JSON array."""
    string = stream.read()
    decoder = json.JSONDecoder().raw_decode
    index = START.match(string, 0).end()

    while index < len(string):
        obj, end = decoder(string, index)
        item = Item()
        item.primitive = obj
        yield item
        index = END.match(string, end).end()


class Writer(Writer):
    """Write Items to a stream as a JSON array."""
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
