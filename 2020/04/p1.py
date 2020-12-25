#!/usr/bin/env python3

import re

valid = 0

req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

with open('input') as f:
    for p in f.read().split('\n\n'):
        fields = set(re.split(r'[: \n]', p)[::2])
        if fields >= req_fields:
            valid += 1
print(valid)
