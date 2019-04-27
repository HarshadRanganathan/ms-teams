from jsonpickle import encode


class AdaptiveCard:
    """
    Root element in an Adaptive Card
    """
    BODY = 'body'

    def __init__(self):
        self.card = dict()
        self.card['type'] = 'AdaptiveCard'
        self.card['$schema'] = 'http://adaptivecards.io/schemas/adaptive-card.json'
        self.card['version'] = '1.0'

    def container(self, container):
        """Containers group items together
        :param container:
        :return:
        """
        if self.BODY not in self.card.keys():
            self.card[self.BODY] = list()
        self.card[self.BODY].append(container)
        return self

    def build(self):
        return encode(self.card, unpicklable=False)
