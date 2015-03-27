import pytest
import io
from entry import Entry
from entry.writer import Writer


def test_writer_interface():
    entry = Entry()
    stream = io.StringIO()

    writer = Writer(stream)

    assert writer.stream == stream

    with pytest.raises(NotImplementedError):
        writer.write(entry)

    writer.close()
