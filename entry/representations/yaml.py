from ..entry import Entry
from ..writer import Writer
import yaml


content_type = 'application/yaml'


def load(self, text):
    """Entry from YAML representation."""
    self.__dict__ = yaml.load(text)


def dump(self):
    """Entry in YAML representation."""
    return yaml.dump(self.primitive, default_flow_style=False)


class Writer(Writer):
    """Write YAML array."""
    def __init__(self, stream, sep="\n"):
        self.stream = stream
        self.sep = sep
        self.sol = ""

    def write(self, entry):
        self.stream.write(
            self.sol
            + yaml.dump([entry.primitive], default_flow_style=False))
        self.sol = self.sep


Entry.yaml = property(dump, load)
