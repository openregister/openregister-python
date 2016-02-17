from datetime import datetime

import numbers


class Entry(object):
    """An Entry, an ordered instance of an item in a register."""
    def __init__(self, entry_number=None, item_hash=None, timestamp=None):
        if not (entry_number is None
                or isinstance(entry_number, numbers.Integral)):
            raise ValueError('entry_number')

        self.entry_number = entry_number
        self.item_hash = item_hash
        self.timestamp = timestamp

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if timestamp is None:
            self._timestamp = datetime.utcnow()
        else:
            self._timestamp = timestamp

    @property
    def primitive(self):
        """Entry as Python primitive."""
        primitive = {}
        if self.entry_number is not None:
            primitive['entry-number'] = self.entry_number

        if self.item_hash is not None:
            primitive['item-hash'] = self.item_hash

        primitive['timestamp'] = self.timestamp
        return primitive

    @primitive.setter
    def primitive(self, primitive):
        """Entry from Python primitive."""
        self.entry_number = primitive['entry-number']
        self.item_hash = primitive['item-hash']
        self.timestamp = datetime.strptime(
            primitive['timestamp'],
            "%Y-%m-%dT%H:%M:%SZ")
