from ..thing import Thing


content_type = None


def load(self, dictionary):
    """Thing from Python primitive."""
    self.__dict__ = dictionary


def dump(self):
    """Python primitive representation."""
    return self.__dict__.copy()


Thing.primitive = property(dump, load)
