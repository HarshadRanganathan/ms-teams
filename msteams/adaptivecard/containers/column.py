from msteams.adaptivecard.containers.layout import Layout


class Column(Layout):
    """
    Containers group items together
    """
    Items = 'items'

    def __init__(self, width=None):
        Layout.__init__(self, 'Column')
        if width is not None:
            self.layout['width'] = width

    def element(self, element):
        """card elements to render inside the Column.
        :param element: card element
        :return:
        """
        if self.Items not in self.layout.keys():
            self.layout[self.Items] = list()
        self.layout[self.Items].append(element)
        return self
