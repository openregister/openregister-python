import io
from thingstance import Thing
from thingstance.representations.tsv import Writer


def test_writer_zero_things():
    out = io.StringIO()
    writer = Writer(out, fieldnames=[])
    writer.close()

    string = out.getvalue()
    assert string == "\n"


def test_writer_zero_things_titles():
    out = io.StringIO()
    writer = Writer(out, fieldnames=['one', 'two', 'three'])
    writer.close()

    string = out.getvalue()
    assert string == 'one\ttwo\tthree\n'


def test_writer_one_thing():
    out = io.StringIO()
    writer = Writer(out, fieldnames=["name"])
    thing = Thing(name="one")
    writer.write(thing)
    writer.close()

    string = out.getvalue()
    assert string == 'name\none\n'


def test_writer_many_things():
    out = io.StringIO()
    writer = Writer(out, fieldnames=["name", "text"])
    for name in ['one', 'two', 'three']:
        thing = Thing(name=name, text="hello world")
        writer.write(thing)
    writer.close()

    string = out.getvalue()
    assert string == (
        'name\ttext\n'
        'one\thello world\n'
        'two\thello world\n'
        'three\thello world\n')
