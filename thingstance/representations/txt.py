from ..thing import Thing
from .yaml import Writer as _Writer
from .yaml import load, dump

content_type = 'text/plain; charset=utf-8'
Writer = _Writer
Thing.txt = property(dump, load)
