from msteams.adaptivecard.containers.layout import Layout


class Container(Layout):
    """
    Containers group items together
    """
    Items = 'items'

    def __init__(self):
        Layout.__init__(self, 'Container')

    def element(self, element):
        """card elements to render inside the Container.
        :param element: card element
        :return:
        """
        if self.Items not in self.layout.keys():
            self.layout[self.Items] = list()
        self.layout[self.Items].append(element)
        return self
