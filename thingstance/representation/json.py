from ..thing import Thing
import json


def dump(self):
    """JSON representation of a Thing."""
    return json.dumps(self.__dict__, sort_keys=True, ensure_ascii=False)


def register():
    Thing.json = property(dump)
