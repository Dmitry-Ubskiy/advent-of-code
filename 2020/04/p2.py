#!/usr/bin/env python3

import re

valid = 0

req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def valid_hgt(hgt):
    if hgt.endswith('cm'):
        return 150 <= int(hgt[:-2]) <= 193
    if hgt.endswith('in'):
        return 59 <= int(hgt[:-2]) <= 76
    return False

validate = {
    'byr': lambda n: 1920 <= int(n) <= 2002,
    'iyr': lambda n: 2010 <= int(n) <= 2020,
    'eyr': lambda n: 2020 <= int(n) <= 2030,
    'hgt': valid_hgt,
    'hcl': lambda s: re.match(r'^#[0-9a-f]{6}$', s) is not None,
    'ecl': lambda s: s in {'amb','blu','brn','gry','grn','hzl','oth'},
    'pid': lambda s: re.match(r'^[0-9]{9}$', s) is not None,
    'cid': lambda x: True
}

with open('input') as f:
    for p in f.read().split('\n\n'):
        tokens = re.split(r'[: \n]', p.strip())
        keys = tokens[0::2]
        values = tokens[1::2]
        if set(keys) >= req_fields:
            fields = dict(zip(keys, values))
            if all(validate[k](fields[k]) for k in keys):
                valid += 1
print(valid)
