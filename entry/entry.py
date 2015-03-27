from .datatypes.digest import git_hash, base32_encode


class Entry(object):
    """An Entry, a content addressable set of attributes."""
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    @property
    def hash(self):
        """The git hash-object value of for the Entry."""
        return git_hash(self.json.encode("utf-8"))

    @property
    def hashkey(self):
        """The hash value as a RFC 3548 Base 32 encoded string."""
        return base32_encode(self.hash)
