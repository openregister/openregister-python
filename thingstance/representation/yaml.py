from ..thing import Thing
import yaml


def dump(self):
    return yaml.dump(self.__dict__, default_flow_style=False)


def register():
    Thing.yaml = property(dump)
