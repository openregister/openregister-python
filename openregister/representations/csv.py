import io
import csv
from ..item import Item
from ..writer import Writer


content_type = 'text/csv; charset=utf-8'
escapechar = '\\'
lineterminator = '\r\n'
quotechar = '"'
delimiter = ","


def load(self, text,
         lineterminator='\r\n',
         quotechar='"',
         delimiter=",",
         escapechar=escapechar,
         quoting=csv.QUOTE_MINIMAL):
    """Item from CSV representation."""

    f = io.StringIO(text)

    if not quotechar:
        quoting = csv.QUOTE_NONE

    reader = csv.DictReader(
        f,
        delimiter=delimiter,
        quotechar=quotechar,
        quoting=quoting,
        lineterminator=lineterminator)

    if reader.fieldnames:
        reader.fieldnames = [field.strip() for field in reader.fieldnames]

    try:
        self.primitive = next(reader)
    except StopIteration:
        self.primitive = {}


class Writer(Writer):
    """Write CSV of entries."""
    def __init__(self, stream, fieldnames,
                 delimiter=delimiter,
                 lineterminator=lineterminator,
                 quotechar=quotechar,
                 escapechar=escapechar,
                 quoting=csv.QUOTE_ALL):

        if not quotechar:
            quoting = csv.QUOTE_NONE

        self.writer = csv.DictWriter(
            stream,
            fieldnames=fieldnames,
            delimiter=delimiter,
            lineterminator=lineterminator,
            escapechar=escapechar,
            quotechar=quotechar,
            quoting=quoting)

        self.writer.writeheader()

    def write(self, item):
        self.writer.writerow(item.primitive)


def dump(self, **kwargs):
    """CSV representation of a item."""

    f = io.StringIO()
    w = Writer(f, self.keys, **kwargs)
    w.write(self)
    text = f.getvalue().lstrip()
    f.close()

    return text


Item.csv = property(dump, load)
