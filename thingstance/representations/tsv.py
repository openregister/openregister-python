from ..thing import Thing
from .csv import load as _load
from .csv import dump as _dump


content_type = 'text/tab-separated-values; charset=utf-8'


def load(self, text, fieldnames=None):
    """Thing from TSV representation."""
    _load(self, text, delimiter="\t", quotechar="", lineterminator='\n')


def dump(self):
    """TSV representation."""
    return _dump(self, delimiter="\t", quotechar=None, lineterminator='\n')


Thing.tsv = property(dump, load)
