from msteams.adaptivecard.elements.element import Element


class Image(Element):
    """
    Displays an image
    """

    def __init__(self, url):
        """
        :param url: The URL to the image.
        :type url: str
        """
        Element.__init__(self, 'Image')
        self.element['url'] = url

    def style(self, style):
        """Controls how this Image is displayed
        :param style:
        :type style: str
        :return:
        """
        self.element['style'] = style
        return self

    def size(self, size):
        """approximate size of the image
        :param size: Controls the approximate size of the image.
        The physical dimensions will vary per host. Specify "auto" for true image dimension, or "stretch" to force it to fill the container.
        :type size: str
        :return:
        """
        self.element['size'] = size
        return self
