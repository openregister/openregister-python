from ..thing import Thing
from ..writer import Writer
import yaml


content_type = 'application/yaml'


def load(self, text):
    """Thing from YAML representation."""
    self.__dict__ = yaml.load(text)


def dump(self):
    """Thing in YAML representation."""
    return yaml.dump(self.primitive, default_flow_style=False)


class Writer(Writer):
    """Write YAML array."""
    def __init__(self, stream, sep="\n"):
        self.stream = stream
        self.sep = sep
        self.sol = ""

    def write(self, thing):
        self.stream.write(
            self.sol
            + yaml.dump([thing.primitive], default_flow_style=False))
        self.sol = self.sep


Thing.yaml = property(dump, load)
