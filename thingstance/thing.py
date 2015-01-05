import json
from hashlib import sha1


class Thing(object):
    """A Thing, a content addressable set of properties."""
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    @property
    def uid(self):
        """The uid value, the git hash-object of the json."""
        data = self.json
        return sha1(
            str("blob "
                + str(len(data))
                + "\0").encode("utf-8")
            + data.encode("utf-8")
            ).hexdigest()

    @property
    def json(self):
        """The canonical representation of the Thing, as json."""
        return json.dumps(self.__dict__, sort_keys=True, ensure_ascii=False)
