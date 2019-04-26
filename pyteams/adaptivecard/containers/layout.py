
class Layout:

    def __init__(self, layout_type):
        self.layout = dict()
        self.layout['type'] = layout_type

    def build(self):
        return self.layout
