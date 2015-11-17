import pytest
import io
from openregister.reader import Reader


def test_writer_interface():
    stream = io.StringIO()

    reader = Reader(stream)

    assert reader.stream == stream

    with pytest.raises(NotImplementedError):
        reader.read()

    reader.close()
