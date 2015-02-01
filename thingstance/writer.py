class Writer(object):

    """Interface for writing a series of Things to a stream."""

    def __init__(self, stream):
        self.stream = stream

    def write(self, thing):
        raise NotImplementedError

    def close(self):
        pass
