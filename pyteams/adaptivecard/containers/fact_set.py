from pyteams.adaptivecard.containers.layout import Layout


class FactSet(Layout):
    """
    FactSet element displays a series of facts (i.e. name/value pairs) in a tabular form
    """

    FACTS = 'facts'

    def __init__(self, spacing=None, separator=None):
        """
        :param spacing: amount of spacing
        :param separator: draw a separating line at the top of the element
        """
        Layout.__init__(self, 'FactSet')
        if spacing is not None:
            self.layout['spacing'] = spacing
        if separator is not None:
            self.layout['separator'] = separator

    def fact(self, fact):
        """Fact as a key/value pair
        :param fact:
        :return:
        """
        if self.FACTS not in self.layout.keys():
            self.layout[self.FACTS] = list()
        self.layout[self.FACTS].append(fact)
        return self
