#! usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os.path import abspath, join

import matplotlib


# let's configure matplotlib's settings
# we have to call matplotlib.use() before we import matplotlib.pyplot
matplotlib.use('TkAgg')

# now let's import matplotlib.pyplot
import matplotlib.pyplot
plt = matplotlib.pyplot

# let's define a helper function that will build a shortcut for our filepaths
SBA_FILE_LOADER = lambda *path: join(abspath('/Users/joshmaccabee/Projects/'
    'strategic_business_analytics/fixtures'), *path)


# let's define a function to quickly print out visual breaks for questions
def line_maker(char='=', count=80):
    return char * count
