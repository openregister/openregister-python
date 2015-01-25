from ..thing import Thing
import io
import csv


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


def dump(self,
         delimiter=",",
         lineterminator='\r\n',
         quotechar='"',
         quoting=csv.QUOTE_ALL):

    """CSV representation."""

    dict = self.primitive

    fieldnames = sorted(list(dict.keys()))

    f = io.StringIO()

    if not quotechar:
        quoting = csv.QUOTE_NONE

    writer = csv.DictWriter(
        f,
        fieldnames=fieldnames,
        delimiter=delimiter,
        lineterminator=lineterminator,
        quotechar=quotechar,
        quoting=quoting)

    writer.writeheader()
    writer.writerow(dict)

    text = f.getvalue().lstrip()
    f.close()

    return text


Thing.csv = property(dump, load)
