#!/usr/bin/env python3

import re

pattern = re.compile(r'^(\d+)-(\d+) (.): (.+)$')
valid = 0
with open('input') as f:
    for line in f:
        lo, hi, ch, pw = pattern.match(line.strip()).groups()
        lo = int(lo) - 1
        hi = int(hi) - 1
        if (pw[lo] + pw[hi]).count(ch) == 1:
            valid += 1
print(valid)

