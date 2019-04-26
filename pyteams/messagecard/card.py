from jsonpickle import encode


class MessageCard:
    """
    Root element in an Message Card
    """
    SECTIONS = 'sections'

    def __init__(self):
        self.card = dict()
        self.card['@type'] = 'MessageCard'
        self.card['@context'] = 'https://schema.org/extensions'

    def title(self, title):
        """content of the card
        :param title:
        :type title: str
        :return:
        """
        self.card['title'] = title
        return self

    def summary(self, summary):
        """determine what the card is all about
        :param summary:
        :type summary: str
        :return:
        """
        self.card['summary'] = summary
        return self

    def theme_color(self, theme_color):
        self.card['themeColor'] = theme_color
        return self

    def section(self, section):
        """sections to include in the card
        :param section:
        :return:
        """
        if self.SECTIONS not in self.card.keys():
            self.card[self.SECTIONS] = list()
        self.card[self.SECTIONS].append(section)
        return self

    def build(self):
        return encode(self.card, unpicklable=False)
