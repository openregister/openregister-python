import io
from openregister import Item
from openregister.representations.tsv import Writer


def test_writer_zero_entries():
    out = io.StringIO()
    writer = Writer(out, fieldnames=[])
    writer.close()

    string = out.getvalue()
    assert string == "\n"


def test_writer_zero_entries_titles():
    out = io.StringIO()
    writer = Writer(out, fieldnames=['one', 'two', 'three'])
    writer.close()

    string = out.getvalue()
    assert string == 'one\ttwo\tthree\n'


def test_writer_one_item():
    out = io.StringIO()
    writer = Writer(out, fieldnames=["name"])
    item = Item(name="one")
    writer.write(item)
    writer.close()

    string = out.getvalue()
    assert string == 'name\none\n'


def test_writer_many_entries():
    out = io.StringIO()
    writer = Writer(out, fieldnames=["name", "text"])
    for name in ['one', 'two', 'three']:
        item = Item(name=name, text="hello world")
        writer.write(item)
    writer.close()

    string = out.getvalue()
    assert string == (
        'name\ttext\n'
        'one\thello world\n'
        'two\thello world\n'
        'three\thello world\n')
