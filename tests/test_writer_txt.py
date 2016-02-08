import io
from openregister import Item
from openregister.representations.txt import Writer


def test_writer_zero_items():
    out = io.StringIO()
    writer = Writer(out)
    writer.close()

    string = out.getvalue()
    assert string == ""


def test_writer_one_item():
    out = io.StringIO()
    writer = Writer(out)
    item = Item(name="one")
    writer.write(item)
    writer.close()

    string = out.getvalue()
    assert string == '- name: one\n'


def test_writer_many_items():
    out = io.StringIO()
    writer = Writer(out)
    for name in ['one', 'two', 'three']:
        item = Item(name=name, text="hello world")
        writer.write(item)
    writer.close()

    string = out.getvalue()
    assert string == ('- name: one\n'
                      '  text: hello world\n'
                      '\n'
                      '- name: two\n'
                      '  text: hello world\n'
                      '\n'
                      '- name: three\n'
                      '  text: hello world\n')
