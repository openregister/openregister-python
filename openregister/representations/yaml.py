from ..item import Item
from ..writer import Writer
import yaml


content_type = 'application/yaml'


def load(self, text):
    """Item from YAML representation."""
    self.__dict__ = yaml.load(text)


def dump(self):
    """Item in YAML representation."""
    return yaml.dump(self.primitive, default_flow_style=False)


class Writer(Writer):
    """Write YAML array."""
    def __init__(self, stream, sep="\n"):
        self.stream = stream
        self.sep = sep
        self.sol = ""

    def write(self, item):
        self.stream.write(
            self.sol
            + yaml.dump([item.primitive], default_flow_style=False))
        self.sol = self.sep


Item.yaml = property(dump, load)
