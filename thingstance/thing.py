from hashlib import sha1


def hash(data):
    head = str("blob " + str(len(data)) + "\0").encode("utf-8")
    digest = sha1(head + data)
    return digest.hexdigest()


class Thing(object):
    """A Thing, a content addressable set of attributes."""
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    @property
    def hash(self):
        """A digest of the Thing; the git hash-object value of the json."""
        return hash(self.json.encode("utf-8"))
