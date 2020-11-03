#!/usr/bin/env python3

import sys, re

for line in sys.stdin:
    line = line.split(' ')
    date = re.search(r'[0-9]{2}/.*/[0-9]{4}:[0-9]{2}', line[3])[0]
    print(f'{date}\t1')