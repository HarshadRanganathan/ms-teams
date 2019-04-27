from msteams.adaptivecard.containers.layout import Layout


class Fact(Layout):
    """
    Describes a Fact in a FactSet as a key/value pair.
    """

    def __init__(self, title, value):
        Layout.__init__(self, 'Fact')
        self.layout['title'] = title
        self.layout['value'] = value
