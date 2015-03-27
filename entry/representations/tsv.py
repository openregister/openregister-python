from ..entry import Entry
from .csv import load as _load
from .csv import dump as _dump
from .csv import Writer as _Writer


content_type = 'text/tab-separated-values; charset=utf-8'


def load(self, text, fieldnames=None):
    """Entry from TSV representation."""
    _load(self, text, delimiter="\t", quotechar="", lineterminator='\n')


def dump(self):
    """TSV representation."""
    return _dump(self, delimiter="\t", quotechar=None, lineterminator='\n')


class Writer(_Writer):
    def __init__(self, stream, fieldnames):
        _Writer.__init__(self, stream,
                         fieldnames=fieldnames,
                         delimiter="\t", quotechar=None, lineterminator='\n')


Entry.tsv = property(dump, load)
