#!/usr/bin/env python3

import re

pattern = re.compile(r'^(\d+)-(\d+) (.): (.+)$')
valid = 0
with open('input') as f:
    for line in f:
        lo, hi, ch, pw = pattern.match(line.strip()).groups()
        if int(lo) <= pw.count(ch) <= int(hi):
            valid += 1
print(valid)
