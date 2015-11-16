from ..item import Item
from ..writer import Writer

content_type = 'text/tab-separated-values; charset=utf-8'

escaped_chars = [('\t', '\\t'), ('\n', '\\n'), ('\r', '\\r'), ('', '\\')]


def BadBackslash():
    pass


def escape(value):
    for a, b in escaped_chars:
        if a:
            value = value.replace(a, b)
    return value


def unescape(value):
    if value[-1:] == '\\':
        raise BadBackslash
    for a, b in escaped_chars:
        value = value.replace(b, a)
    return value


def load_line(line):
    return [unescape(s) for s in line.split('\t')]


def load(self, text, fieldnames=None):
    """Item from TSV representation."""
    lines = text.split('\n')
    fieldnames = load_line(lines[0])
    values = load_line(lines[1])
    self.__dict__ = dict(zip(fieldnames, values))


def dump_line(values):
    return ('\t'.join(escape(value) for value in values)) + '\n'


def dump(self):
    """TSV representation."""
    dict = self.primitive
    if not dict:
        return ''
    return dump_line(self.keys) + dump_line(self.values)


class Writer(Writer):
    def __init__(self, stream, fieldnames):
        self.stream = stream
        self.stream.write(dump_line(fieldnames))

    def write(self, item):
        self.stream.write(dump_line(item.values))


Item.tsv = property(dump, load)
