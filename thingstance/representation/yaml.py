from ..thing import Thing
import yaml


def load(self, text):
    """Thing from YAML representation."""
    self.__dict__ = yaml.load(text)


def dump(self):
    """Thing in YAML representation."""
    return yaml.dump(self.__dict__, default_flow_style=False)


def register():
    Thing.yaml = property(dump, load)
