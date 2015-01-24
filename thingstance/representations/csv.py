from ..thing import Thing
import io
import csv


content_type = 'text/csv; charset=utf-8'


def load(self, text, delimiter=",", fieldnames=None):
    """Thing from CSV representation."""
    self.__dict__ = {}
    f = io.StringIO(text)
    reader = csv.DictReader(f, fieldnames)
    self.__dict__ = {}
    for dict in reader:
        self.__dict__ = dict
        break


def dump(self):
    """CSV representation."""

    dict = self.primitive

    fieldnames = sorted(list(dict.keys()))
    delimiter = ','
    quoting = csv.QUOTE_ALL
    quotechar = '"'

    f = io.StringIO()

    writer = csv.DictWriter(
        f,
        fieldnames=fieldnames,
        delimiter=delimiter,
        quotechar=quotechar,
        quoting=quoting)

    writer.writeheader()
    writer.writerow(dict)

    text = f.getvalue()
    f.close()

    return text


Thing.csv = property(dump, load)
