from ..thing import Thing
import json


def set_default(obj):
    if isinstance(obj, set):
        return sorted(list(obj))
    raise TypeError


def dump(self):
    """JSON representation."""
    return json.dumps(
        self.__dict__,
        sort_keys=True,
        ensure_ascii=False,
        default=set_default)


def register():
    Thing.json = property(dump)
