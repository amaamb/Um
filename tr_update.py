#!/usr/bin/env python
import os
import sys
if sys.platform == 'win32':
    pybabel = 've\\Scripts\\pybabel'
else:
    pybabel = 've/bin/pybabel'
os.system(pybabel + ' extract -F babel.cfg -k lazy_gettext -o messages.pot main')
os.system(pybabel + ' update -i messages.pot -d main/translations')
os.unlink('messages.pot')
