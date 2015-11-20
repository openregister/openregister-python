import pytest
import io
from openregister.representations.jsonl import reader


def test_reader_zero_entries():
    stream = io.StringIO("")
    with pytest.raises(StopIteration):
        next(reader(stream))


def test_reader_one_item():
    stream = io.StringIO('  { "name": "one" }')
    items = reader(stream)

    assert items.__next__().json == '{"name":"one"}'

    with pytest.raises(StopIteration):
        items.__next__()


def test_reader_many_items():
    stream = io.StringIO('{"name":"one"}\n'
                         '{"name":"two"}\n'
                         '{"name":"three"}\n')

    items = reader(stream)
    assert (items.__next__()).json == '{"name":"one"}'
    assert (items.__next__()).json == '{"name":"two"}'
    assert (items.__next__()).json == '{"name":"three"}'

    with pytest.raises(StopIteration):
        items.__next__()
