import io
import csv
from ..thing import Thing
from ..writer import Writer


content_type = 'text/csv; charset=utf-8'


def load(self, text,
         lineterminator='\r\n',
         quotechar='"',
         delimiter=",",
         quoting=csv.QUOTE_MINIMAL):
    """Thing from CSV representation."""

    f = io.StringIO(text)

    if not quotechar:
        quoting = csv.QUOTE_NONE

    reader = csv.DictReader(
        f,
        delimiter=delimiter,
        quotechar=quotechar,
        quoting=quoting,
        lineterminator=lineterminator)

    try:
        self.primitive = next(reader)
    except StopIteration:
        self.primitive = {}


class Writer(Writer):
    """Write CSV of things."""
    def __init__(self, stream, fieldnames,
                 delimiter=",",
                 lineterminator='\r\n',
                 quotechar='"',
                 quoting=csv.QUOTE_ALL):

        if not quotechar:
            quoting = csv.QUOTE_NONE

        self.writer = csv.DictWriter(
            stream,
            fieldnames=fieldnames,
            delimiter=delimiter,
            lineterminator=lineterminator,
            quotechar=quotechar,
            quoting=quoting)

        self.writer.writeheader()

    def write(self, thing):
        self.writer.writerow(thing.primitive)


def dump(self, **kwargs):
    """CSV representation of a thing."""

    fieldnames = sorted(list(self.primitive.keys()))

    f = io.StringIO()
    w = Writer(f, fieldnames, **kwargs)
    w.write(self)
    text = f.getvalue().lstrip()
    f.close()

    return text


Thing.csv = property(dump, load)
