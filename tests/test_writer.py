import pytest
from thingstance import Thing
from thingstance.writer import Writer


def test_writer_interface():
    thing = Thing()

    writer = Writer('stream')

    assert writer.stream == 'stream'

    with pytest.raises(NotImplementedError):
        writer.write(thing)

    writer.close()
