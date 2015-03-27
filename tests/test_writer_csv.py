import io
from entry import Entry
from entry.representations.csv import Writer


def test_writer_zero_things():
    out = io.StringIO()
    writer = Writer(out, fieldnames=[])
    writer.close()

    string = out.getvalue()
    assert string == "\r\n"


def test_writer_zero_things_titles():
    out = io.StringIO()
    writer = Writer(out, fieldnames=['one', 'two', 'three'])
    writer.close()

    string = out.getvalue()
    assert string == '"one","two","three"\r\n'


def test_writer_one_thing():
    out = io.StringIO()
    writer = Writer(out, fieldnames=["name"])
    entry = Entry(name="one")
    writer.write(entry)
    writer.close()

    string = out.getvalue()
    assert string == '"name"\r\n"one"\r\n'


def test_writer_many_things():
    out = io.StringIO()
    writer = Writer(out, fieldnames=["name", "text"])
    for name in ['one', 'two', 'three']:
        entry = Entry(name=name, text="hello world")
        writer.write(entry)
    writer.close()

    string = out.getvalue()
    assert string == (
        '"name","text"\r\n'
        '"one","hello world"\r\n'
        '"two","hello world"\r\n'
        '"three","hello world"\r\n')
