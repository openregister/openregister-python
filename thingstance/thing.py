from hashlib import sha1


class Thing(object):
    """A Thing, a content addressable set of attributes."""
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    @property
    def hash(self):
        """A digest of the Thing; the git hash-object value of the json."""
        data = self.json.encode("utf-8")
        head = str("blob " + str(len(data)) + "\0").encode("utf-8")
        return sha1(head + data).hexdigest()
