from copy import copy
from ..entry import Entry


content_type = None


def load(self, dictionary):
    """Entry from Python primitive."""
    self.__dict__ = dictionary


def dump(self):
    """Python primitive representation."""
    dict = {}
    for key, value in self.__dict__.items():
        if not key.startswith('_'):
            dict[key] = copy(value)

    for key in dict:
        if isinstance(dict[key], (set)):
            dict[key] = sorted(list(dict[key]))

    return dict


Entry.primitive = property(dump, load)
