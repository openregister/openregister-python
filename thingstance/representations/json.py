from ..thing import Thing
import json


content_type = 'application/json'


def load(self, text):
    """Thing from JSON representation."""
    self.__dict__ = json.loads(text)


def dump(self):
    """JSON representation."""
    return json.dumps(
        self.primitive,
        sort_keys=True,
        ensure_ascii=False)


Thing.json = property(dump, load)
