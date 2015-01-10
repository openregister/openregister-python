from .datatypes.digest import hash


class Thing(object):
    """A Thing, a content addressable set of attributes."""
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    @property
    def hash(self):
        """The git hash-object value of the json."""
        return hash(self.json.encode("utf-8"))
