import pytest
import io
from openregister.representations.tsv import reader


def test_reader_zero_entries():
    stream = io.StringIO("")
    with pytest.raises(StopIteration):
        next(reader(stream))


def test_reader_one_item():
    stream = io.StringIO("name\n" "one\n")
    items = reader(stream)

    assert items.__next__().json == '{"name":"one"}'

    with pytest.raises(StopIteration):
        items.__next__()


def test_reader_many_items():
    stream = io.StringIO("name\ttext\n"
                         "one\t1\n"
                         "two\t2\n"
                         "three\t3\n")

    items = reader(stream)
    assert (items.__next__()).json == '{"name":"one","text":"1"}'
    assert (items.__next__()).json == '{"name":"two","text":"2"}'
    assert (items.__next__()).json == '{"name":"three","text":"3"}'

    with pytest.raises(StopIteration):
        items.__next__()


def test_reader_encoded_newline():
    stream = io.StringIO("name\ttext\n" "one\tOne line\\nAnother line\n")
    items = reader(stream)

    item = items.__next__()
    assert item.text == "One line\nAnother line"

    with pytest.raises(StopIteration):
        items.__next__()
