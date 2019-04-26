
class Element:

    def __init__(self, type):
        self.element = dict()
        self.element['type'] = type

    def build(self):
        return self.element
