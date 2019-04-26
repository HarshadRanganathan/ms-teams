from pyteams.adaptivecard.containers.layout import Layout


class ColumnSet(Layout):
    """
    ColumnSet divides a region into Columns, allowing elements to sit side-by-side
    """
    COLUMNS = 'columns'

    def __init__(self, spacing=None, separator=None):
        Layout.__init__(self, 'ColumnSet')
        if spacing is not None:
            self.layout['spacing'] = spacing
        if separator is not None:
            self.layout['separator'] = separator

    def column(self, column):
        """container that is part of a ColumnSet.
        :param column:
        :return:
        """
        if self.COLUMNS not in self.layout.keys():
            self.layout[self.COLUMNS] = list()
        self.layout[self.COLUMNS].append(column)
        return self
