import io
import csv
from ..entry import Entry
from ..writer import Writer


content_type = 'text/csv; charset=utf-8'


def load(self, text,
         lineterminator='\r\n',
         quotechar='"',
         delimiter=",",
         quoting=csv.QUOTE_MINIMAL):
    """Entry from CSV representation."""

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

    def write(self, entry):
        self.writer.writerow(entry.primitive)


def dump(self, **kwargs):
    """CSV representation of a entry."""

    fieldnames = sorted(list(self.primitive.keys()))

    f = io.StringIO()
    w = Writer(f, fieldnames, **kwargs)
    w.write(self)
    text = f.getvalue().lstrip()
    f.close()

    return text


Entry.csv = property(dump, load)
