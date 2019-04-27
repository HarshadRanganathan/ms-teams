import os
import pytest

from json import load, loads
from msteams.adaptivecard.elements.image import Image
from msteams.adaptivecard.elements.text_block import TextBlock
from msteams.adaptivecard.containers.column import Column
from msteams.adaptivecard.containers.column_set import ColumnSet
from msteams.adaptivecard.containers.container import Container
from msteams.adaptivecard.containers.fact_set import FactSet
from msteams.adaptivecard.containers.fact import Fact
from msteams.adaptivecard.card import AdaptiveCard

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


@pytest.fixture()
def expected_payload():
    with open(os.path.join(__location__, 'adaptive_card_payload.json'), 'r') as f:
        yield load(f)


def test_adaptive_card(expected_payload):
    title = TextBlock('ms-teams').separator(True).size('Medium').weight('Bolder').build()

    activity_image = Image('https://www.shareicon.net/data/32x32/2016/07/16/634601_python_512x512.png').style('Person').size('small').build()
    activity_title = TextBlock('Description').weight('Bolder').wrap(True).build()
    activity_text = TextBlock('Helper library to construct microsoft teams connector card messages').spacing('None').wrap(True).build()

    activity_image_col = Column('auto').element(activity_image).build()
    activity_text_col = Column('stretch').element(activity_title).element(activity_text).build()
    activity_grp = ColumnSet().column(activity_image_col).column(activity_text_col).build()

    header = Container().element(title).element(activity_grp).build()
    adaptive_card = AdaptiveCard().container(header)

    pkg_info = Container()

    basic = FactSet(separator=True)\
        .fact(Fact('URL', 'https://github.com/HarshadRanganathan/ms-teams').build()) \
        .fact(Fact('AUTHOR', 'Harshad Ranganathan').build()) \
        .fact(Fact('LICENSE', 'MIT').build()) \
        .build()

    keywords = FactSet(separator=True) \
        .fact(Fact('KEYWORDS', 'Microsoft Teams').build()) \
        .build()

    classifiers = FactSet(separator=True) \
        .fact(Fact('CLASSIFIERS', 'Programming Language :: Python :: 3.7\n\n'
                                  'License :: OSI Approved :: MIT License\n\n'
                                  'Operating System :: OS Independent').build()) \
        .build()

    pkg_info.element(basic)
    pkg_info.element(keywords)
    pkg_info.element(classifiers)

    body = pkg_info.build()

    payload = adaptive_card.container(body).build()
    print(payload)
    assert loads(payload) == expected_payload
