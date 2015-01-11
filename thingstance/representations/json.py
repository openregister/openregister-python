from ..thing import Thing
import json


content_type = 'application/json'


def load(self, text):
    """Thing from JSON representation."""
    self.__dict__ = json.loads(text)


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


Thing.json = property(dump, load)
