from ..thing import Thing
from ..writer import Writer
import json


content_type = 'application/json'


def load(self, text):
    """Thing from JSON representation."""
    self.__dict__ = json.loads(text)


def dump(self, eol="\n"):
    """JSON representation."""
    return json.dumps(
        self.primitive,
        sort_keys=True,
        ensure_ascii=False) + eol


class Writer(Writer):
    """Write JSON array."""
    def __init__(self, stream, start="[", sep=",\n", end="]\n"):
        self.stream = stream
        self.sep = sep
        self.end = end
        self.stream.write(start)
        self.sol = ""

    def write(self, thing):
        self.stream.write(self.sol + dump(thing, eol=""))
        self.sol = self.sep

    def close(self):
        self.stream.write(self.end)


Thing.json = property(dump, load)
