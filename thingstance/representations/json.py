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
    def __init__(self, stream, sof="[", sep=",\n", eof="]\n"):
        self.stream = stream
        self.sep = sep
        self.eof = eof
        self.stream.write(sof)
        self.sol = ""

    def write(self, thing):
        self.stream.write(self.sol + dump(thing, eol=""))
        self.sol = self.sep

    def close(self):
        self.stream.write(self.eof)


Thing.json = property(dump, load)
