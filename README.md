# pyteams

Helper library to construct microsoft teams connector card messages.

This library supports building:
1. [Legacy Message Card](https://docs.microsoft.com/en-us/outlook/actionable-messages/message-card-reference)
2. [Adaptive Message Card](https://docs.microsoft.com/en-us/outlook/actionable-messages/adaptive-card) (Not yet supported in teams connector)

## Usage

### Legacy Message Card

Let's build below message card using pyteams library.

![Message Card](images/Message_Card.png?raw=true)

```python
# imports
from pyteams.messagecard.fact import Fact
from pyteams.messagecard.section import Section
from pyteams.messagecard.card import MessageCard

# Create Activity Section
activity_section = Section()\
	.activity_group(activity_image='https://www.shareicon.net/data/32x32/2016/07/16/634601_python_512x512.png',
                    activity_title='Description',
                    activity_text='Helper library to construct microsoft teams connector card messages')\
    .build()

# Add activitity section to the message card
message_card = MessageCard().title('pyteams')\
    .summary('Helper library to construct microsoft teams connector card messages')\
    .theme_color('FF0000')\
    .section(activity_section)

# Create facts
pkg_info = Section()\
    .fact(Fact('URL', 'https://github.com/HarshadRanganathan/pyteams').build())\
    .fact(Fact('AUTHOR', 'Harshad Ranganathan').build())\
    .build()

# Add facts to the message card and construct the message
payload = message_card.section(pkg_info).build()
```


### Adaptive Card

You can use [Card Playground](https://messagecardplayground.azurewebsites.net/) to craft your adaptive cards and build your messages.

Refer [Adaptive Card Schema](https://docs.microsoft.com/en-us/adaptive-cards/authoring-cards/card-schema) for authoring your cards. 

Let's build below adaptive card using pyteams library.

![Adaptive Card](images/Adaptive_Card.png?raw=true)

```python
# imports
from pyteams.adaptivecard.elements.image import Image
from pyteams.adaptivecard.elements.text_block import TextBlock
from pyteams.adaptivecard.containers.column import Column
from pyteams.adaptivecard.containers.column_set import ColumnSet
from pyteams.adaptivecard.containers.container import Container
from pyteams.adaptivecard.containers.fact_set import FactSet
from pyteams.adaptivecard.containers.fact import Fact
from pyteams.adaptivecard.card import AdaptiveCard

# Create Title using TextBlock (Displays text, allowing control over font sizes, weight, and color.)
title = TextBlock('pyteams').separator(True).size('Medium').weight('Bolder').build()

# Create Activity Block (Image, Title, Subtitle)
activity_image = Image('https://www.shareicon.net/data/32x32/2016/07/16/634601_python_512x512.png').style('Person').size('small').build()
activity_title = TextBlock('Description').weight('Bolder').wrap(True).build()
activity_text = TextBlock('Helper library to construct microsoft teams connector card messages').spacing('None').wrap(True).build()

# Create ColumnSet which allows elements to sit side-by-side
activity_image_col = Column('auto').element(activity_image).build()
activity_text_col = Column('stretch').element(activity_title).element(activity_text).build()
activity_grp = ColumnSet().column(activity_image_col).column(activity_text_col).build()

# Create Container to group items together
header = Container().element(title).element(activity_grp).build()

# Add the container to the adaptive card
adaptive_card = AdaptiveCard().container(header)

# Add series of facts to the Container
pkg_info = Container()

basic = FactSet(separator=True)\
	.fact(Fact('URL', 'https://github.com/HarshadRanganathan/pyteams').build()) \
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

# Build the container
body = pkg_info.build()

# Add facts container to the adaptive card and generate the payload message
payload = adaptive_card.container(body).build()
```