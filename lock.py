#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Hello.

Usage:
  main.py <lock_file> <time_limit>

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
arguments = docopt(__doc__)

import sys
import time
import os
path = arguments['<lock_file>']
limit = int(arguments['<time_limit>'])
for i in range(limit):
    if not os.path.exists(path):
        open(path, 'w').close()
        print('locked')
        break
    else:
        time.sleep(1)
else:
    print('failed')
