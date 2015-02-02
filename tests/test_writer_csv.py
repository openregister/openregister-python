import io
from thingstance import Thing
from thingstance.representations.csv import Writer


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
    thing = Thing(name="one")
    writer.write(thing)
    writer.close()

    string = out.getvalue()
    assert string == '"name"\r\n"one"\r\n'


def test_writer_many_things():
    out = io.StringIO()
    writer = Writer(out, fieldnames=["name", "text"])
    for name in ['one', 'two', 'three']:
        thing = Thing(name=name, text="hello world")
        writer.write(thing)
    writer.close()

    string = out.getvalue()
    assert string == (
        '"name","text"\r\n'
        '"one","hello world"\r\n'
        '"two","hello world"\r\n'
        '"three","hello world"\r\n')
