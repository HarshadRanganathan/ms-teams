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
        :param title: The title property is meant to be rendered in a prominent way, at the very top of the card.
        Use it to introduce the content of the card in such a way users will immediately know what to expect.
        :type title: str
        :return:
        """
        self.card['title'] = title
        return self

    def summary(self, summary):
        """determine what the card is all about
        :param summary: The summary property is typically displayed in the list view in Outlook,
        as a way to quickly determine what the card is all about
        :type summary: str
        :return:
        """
        self.card['summary'] = summary
        return self

    def theme_color(self, theme_color):
        """brand color for the card
        :param theme_color: Specifies a custom brand color for the card. The color will be displayed in a non-obtrusive manner.
        :type theme_color: str
        :return:
        """
        self.card['themeColor'] = theme_color
        return self

    def section(self, section):
        """sections to include in the card
        :param section:
        :type section: dict
        :return:
        """
        if self.SECTIONS not in self.card.keys():
            self.card[self.SECTIONS] = list()
        self.card[self.SECTIONS].append(section)
        return self

    def build(self):
        return encode(self.card, unpicklable=False)
