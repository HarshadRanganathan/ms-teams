import os
import pytest

from json import load, loads
from pyteams.messagecard.fact import Fact
from pyteams.messagecard.section import Section
from pyteams.messagecard.card import MessageCard

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


@pytest.fixture()
def expected_payload():
    with open(os.path.join(__location__, 'message_card_payload.json'), 'r') as f:
        yield load(f)


def test_message_card(expected_payload):
    activity_section = Section()\
        .activity_group(activity_image='https://www.shareicon.net/data/32x32/2016/07/16/634601_python_512x512.png',
                        activity_title='Description',
                        activity_text='Helper library to construct microsoft teams connector card messages')\
        .build()

    message_card = MessageCard().title('pyteams')\
        .summary('Helper library to construct microsoft teams connector card messages')\
        .theme_color('FF0000')\
        .section(activity_section)

    pkg_info = Section()\
        .fact(Fact('URL', 'https://github.com/HarshadRanganathan/pyteams').build())\
        .fact(Fact('AUTHOR', 'Harshad Ranganathan').build())\
        .build()

    payload = message_card.section(pkg_info).build()
    print(payload)
    assert loads(payload) == expected_payload
