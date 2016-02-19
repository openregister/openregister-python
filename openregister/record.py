from .item import Item
from .entry import Entry
from copy import copy


class Record(object):
    """
    A Record, the tuple of an entry and it's item
    Records are useful for representing the latest entry for a
    field value.

    Records are serialised as the merged entry and item
    """
    def __init__(self, entry=None, item=None):
        self.entry = entry
        self.item = item

    @property
    def primitive(self):
        """Record as Python primitive."""
        primitive = copy(self.item.primitive)
        primitive.update(self.entry.primitive)
        return primitive

    @primitive.setter
    def primitive(self, primitive):
        """Record from Python primitive."""
        self.entry = Entry()
        self.entry.primitive = primitive

        primitive = copy(primitive)
        for field in self.entry.fields:
            del primitive[field]

        self.item = Item()
        self.item.primitive = primitive
