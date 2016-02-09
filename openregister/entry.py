import datetime


class Entry(object):
    """An Entry, an ordered instance of an item in a register."""
    def __init__(self, entry_number, item_hash, timestamp=None):
        self.entry_number = entry_number
        self.item_hash = item_hash
        if timestamp is None:
            self.timestamp = datetime.datetime.now()
