#! usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os.path import abspath, join


# let's define a helper function that will build a shortcut for our filepaths
SBA_FILE_LOADER = lambda *path: join(abspath('/Users/joshmaccabee/Projects/'
    'strategic_business_analytics/fixtures'), *path)
