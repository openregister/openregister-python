from ..entry import Entry
from .yaml import Writer as _Writer
from .yaml import load, dump

content_type = 'text/plain; charset=utf-8'
Writer = _Writer
Entry.txt = property(dump, load)
