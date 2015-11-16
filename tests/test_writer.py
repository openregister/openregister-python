import pytest
import io
from openregister import Item
from openregister.writer import Writer


def test_writer_interface():
    item = Item()
    stream = io.StringIO()

    writer = Writer(stream)

    assert writer.stream == stream

    with pytest.raises(NotImplementedError):
        writer.write(item)

    writer.close()
