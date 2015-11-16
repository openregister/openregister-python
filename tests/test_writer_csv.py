import io
from openregister import Item
from openregister.representations.csv import Writer


def test_writer_zero_entries():
    out = io.StringIO()
    writer = Writer(out, fieldnames=[])
    writer.close()

    string = out.getvalue()
    assert string == "\r\n"


def test_writer_zero_entries_titles():
    out = io.StringIO()
    writer = Writer(out, fieldnames=['one', 'two', 'three'])
    writer.close()

    string = out.getvalue()
    assert string == '"one","two","three"\r\n'


def test_writer_one_item():
    out = io.StringIO()
    writer = Writer(out, fieldnames=["name"])
    item = Item(name="one")
    writer.write(item)
    writer.close()

    string = out.getvalue()
    assert string == '"name"\r\n"one"\r\n'


def test_writer_many_entries():
    out = io.StringIO()
    writer = Writer(out, fieldnames=["name", "text"])
    for name in ['one', 'two', 'three']:
        item = Item(name=name, text="hello world")
        writer.write(item)
    writer.close()

    string = out.getvalue()
    assert string == (
        '"name","text"\r\n'
        '"one","hello world"\r\n'
        '"two","hello world"\r\n'
        '"three","hello world"\r\n')
