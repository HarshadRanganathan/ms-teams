from pyteams.adaptivecard.elements.element import Element


class TextBlock(Element):
    """
    Displays text, allowing control over font sizes, weight, and color
    """

    def __init__(self, text):
        """
        :param text:
        :type text: str
        """
        Element.__init__(self, 'TextBlock')
        self.element['text'] = text

    def spacing(self, spacing):
        """
        :param spacing:
        :type spacing: str
        :return:
        """
        self.element['spacing'] = spacing
        return self

    def size(self, size):
        """
        :param size:
        :type size: str
        :return:
        """
        self.element['size'] = size
        return self

    def weight(self, weight):
        """weight of TextBlock elements
        :param weight:
        :type weight: str
        :return:
        """
        self.element['weight'] = weight
        return self

    def wrap(self, wrap):
        """allow text to wrap
        :param wrap:
        :type wrap: bool
        :return:
        """
        self.element['wrap'] = wrap
        return self

    def separator(self, separator):
        """draw a separating line
        :param separator:
        :type separator: bool
        :return:
        """
        self.element['separator'] = separator
        return self

    def isSubtle(self, isSubtle):
        """text slightly toned down to appear less prominent
        :param isSubtle:
        :type isSubtle: bool
        :return:
        """
        self.element['isSubtle'] = isSubtle
        return self

    def build(self):
        return self.element
