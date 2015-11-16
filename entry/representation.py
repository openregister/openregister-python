"""Model interface for a representation module."""

from reader import Reader
from writer import Writer

content_type = 'text/plain; charset=utf-8'
name = "unknown"
suffix = ".unknown"


def dump(self):
    raise NotImplementedError


def load(self):
    raise NotImplementedError


class Reader(Reader):
    pass


class Writer(Writer):
    pass


# register this representation as Entry properties
#
# Entry.unknown = property(dump, load)
