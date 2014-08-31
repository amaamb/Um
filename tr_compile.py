#!/usr/bin/env python
import os
import sys
if sys.platform == 'win32':
    pybabel = 've\\Scripts\\pybabel'
else:
    pybabel = 've/bin/pybabel'
os.system(pybabel + ' compile -d main/translations')
