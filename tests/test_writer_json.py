import io
from openregister import Item
from openregister.representations.json import Writer


def test_writer_zero_items():
    out = io.StringIO()
    writer = Writer(out)
    writer.close()

    string = out.getvalue()
    assert string == "[]"


def test_writer_one_item():
    out = io.StringIO()
    writer = Writer(out)
    item = Item(name="one")
    writer.write(item)
    writer.close()

    string = out.getvalue()
    assert string == '[{"name":"one"}]'


def test_writer_many_items():
    out = io.StringIO()
    writer = Writer(out)
    for name in ['one', 'two', 'three']:
        item = Item(name=name)
        writer.write(item)
    writer.close()

    string = out.getvalue()
    assert string == ('['
                      '{"name":"one"},'
                      '{"name":"two"},'
                      '{"name":"three"}]')
