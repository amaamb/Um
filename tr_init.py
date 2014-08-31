#!/usr/bin/env python

import os
import sys
if sys.platform == 'win32':
    pybabel = 've\\Scripts\\pybabel'
else:
    pybabel = 've/bin/pybabel'
if len(sys.argv) != 2:
    print "usage: tr_init <language-code>"
    sys.exit(1)
os.system(pybabel + ' extract -F babel.cfg -k lazy_gettext -o messages.pot main')
os.system(pybabel + ' init -i messages.pot -d main/translations -l ' + sys.argv[1])
os.unlink('messages.pot')
