import datetime

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

        if self.timestamp is None:
            self.timestamp = datetime.datetime.now()

    @property
    def primitive(self):
        """Python primitive representation."""
        dict = {}
        dict['entry_number'] = self.entry_number
        dict['item_hash'] = self.item_hash
        dict['timestamp'] = self.timestamp
        return dict
