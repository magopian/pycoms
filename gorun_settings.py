#!/usr/bin/env python
# -*- coding: utf-8 -*-

DIRECTORIES = (
    ('./', 'pelican --s settings.py -t theme content/'),
) 
IGNORE_DIRECTORIES = ('output/', 'theme/sass/', '.git/')
IGNORE_EXTENSIONS = ('swp',)
