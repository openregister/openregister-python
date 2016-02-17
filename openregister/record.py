class Record(object):
    """
    A Record, the latest entry containing the given field value

    Records are serialised as the tuple of the entry and the item data
    """
    def __init__(self, field, value, entry, item=None):
        self.field = field
        self.value = value
        self.entry = entry
        self.item = item

    @property
    def primitive(self):
        """Record as Python primitive."""
        primitive = {}
        primitive['entry'] = self.entry
        primitive['item'] = self.item
        return primitive

    @primitive.setter
    def primitive(self, primitive):
        """Record from Python primitive."""
        self.entry = primitive['entry']
        self.item = primitive['item']
