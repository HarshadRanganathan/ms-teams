
class Fact:
    """
    Describes a Fact as a key/value pair.
    """

    def __init__(self, name, value):
        self.fact = dict()
        self.fact['name'] = name
        self.fact['value'] = value

    def build(self):
        return self.fact
