
class Section:
    """
    Sections to include in the card.
    """
    FACTS = 'facts'

    def __init__(self):
        self.section = dict()

    def activity_group(self, activity_image=None, activity_title=None, activity_subtitle=None, activity_text=None):
        """Activity group displayed in a two column layout
        :param activity_image: picture
        :type activity_image: str
        :param activity_title: summarize
        :type activity_title: str
        :param activity_subtitle: subdued content
        :type activity_subtitle: str
        :param activity_text: activity details
        :type activity_text: str
        :return:
        """
        if activity_image is not None:
            self.section['activityImage'] = activity_image
        if activity_title is not None:
            self.section['activityTitle'] = activity_title
        if activity_subtitle is not None:
            self.section['activitySubtitle'] = activity_subtitle
        if activity_text is not None:
            self.section['activityText'] = activity_text
        return self

    def fact(self, fact):
        """name/value pair of fact
        :param fact:
        :return:
        """
        if self.FACTS not in self.section.keys():
            self.section[self.FACTS] = list()
        self.section[self.FACTS].append(fact)
        return self

    def build(self):
        return self.section
