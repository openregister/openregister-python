from ..thing import Thing
import yaml


def dump(self):
    return yaml.dump(self.__dict__, default_flow_style=False)


def stream_load(stream):
    block = stream.readline()
    cont = 1
    while cont:
        line = stream.readline()
        if len(line) == 0:
            cont = 0
        else:
            if line.startswith(' '):
                block = block + line
            else:
                yield block
                block = line


def register():
    Thing.yaml = property(dump)
