class Reader(object):

    """Interface for reading a series of items from a stream."""

    def __init__(self, stream):
        self.stream = stream

    def read(self):
        raise NotImplementedError

    def close(self):
        pass
