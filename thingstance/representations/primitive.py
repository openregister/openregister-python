from ..thing import Thing


content_type = None


def load(self, dictionary):
    """Thing from Python primitive."""
    self.__dict__ = dictionary


def dump(self):
    """Python primitive representation."""
    dict = self.__dict__.copy()
    for key in dict:
        if isinstance(dict[key], (set)):
            dict[key] = sorted(list(dict[key]))

    return dict


Thing.primitive = property(dump, load)
