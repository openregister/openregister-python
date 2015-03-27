import io
from entry import Entry
from entry.representations.yaml import Writer


def test_writer_zero_things():
    out = io.StringIO()
    writer = Writer(out)
    writer.close()

    string = out.getvalue()
    assert string == ""


def test_writer_one_thing():
    out = io.StringIO()
    writer = Writer(out)
    entry = Entry(name="one")
    writer.write(entry)
    writer.close()

    string = out.getvalue()
    assert string == '- name: one\n'


def test_writer_many_things():
    out = io.StringIO()
    writer = Writer(out)
    for name in ['one', 'two', 'three']:
        entry = Entry(name=name, text="hello world")
        writer.write(entry)
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
