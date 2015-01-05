class Thingstance(object):
    """An instance of a Thing, with metadata."""
    name = None
    type = "Thing"
    thing = None
    tags = set()

    def __init__(self, thing):
        self.thing = thing
