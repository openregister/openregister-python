import io
from thingstance import Thing
from thingstance.representations.json import Writer


def test_writer_zero_things():
    out = io.StringIO()
    writer = Writer(out)
    writer.close()

    string = out.getvalue()
    assert string == "[]\n"


def test_writer_one_thing():
    out = io.StringIO()
    writer = Writer(out)
    thing = Thing(name="one")
    writer.write(thing)
    writer.close()

    string = out.getvalue()
    assert string == '[{"name": "one"}]\n'


def test_writer_many_things():
    out = io.StringIO()
    writer = Writer(out)
    for name in ['one', 'two', 'three']:
        thing = Thing(name=name)
        writer.write(thing)
    writer.close()

    string = out.getvalue()
    assert string == ('['
                      '{"name": "one"},\n'
                      '{"name": "two"},\n'
                      '{"name": "three"}]\n')