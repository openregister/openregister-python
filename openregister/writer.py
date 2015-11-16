class Writer(object):

    """Interface for writing a series of Entries to a stream."""

    def __init__(self, stream):
        self.stream = stream

    def write(self, item):
        raise NotImplementedError

    def close(self):
        pass
