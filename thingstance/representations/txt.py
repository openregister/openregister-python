from ..thing import Thing
from .yaml import load, dump


content_type = 'text/plain; charset=utf-8'
Thing.txt = property(dump, load)
