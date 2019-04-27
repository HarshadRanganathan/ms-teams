from msteams.adaptivecard.elements.element import Element


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
        :param spacing: Controls the amount of spacing between this element and the preceding element.
        :type spacing: str
        :return:
        """
        self.element['spacing'] = spacing
        return self

    def size(self, size):
        """
        :param size: Controls size of text.
        :type size: str
        :return:
        """
        self.element['size'] = size
        return self

    def weight(self, weight):
        """weight of TextBlock elements
        :param weight: Controls the weight of TextBlock elements.
        :type weight: str
        :return:
        """
        self.element['weight'] = weight
        return self

    def wrap(self, wrap):
        """allow text to wrap
        :param wrap: If true, allow text to wrap. Otherwise, text is clipped.
        :type wrap: bool
        :return:
        """
        self.element['wrap'] = wrap
        return self

    def separator(self, separator):
        """draw a separating line
        :param separator: When true, draw a separating line at the top of the element.
        :type separator: bool
        :return:
        """
        self.element['separator'] = separator
        return self

    def is_subtle(self, is_subtle):
        """text slightly toned down to appear less prominent
        :param is_subtle: If true, displays text slightly toned down to appear less prominent.
        :type is_subtle: bool
        :return:
        """
        self.element['isSubtle'] = is_subtle
        return self

    def build(self):
        return self.element
