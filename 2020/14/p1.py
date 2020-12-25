#!/usr/bin/env python3

import re

def mask(n, m): 
    return (n & int(m.replace('X', '1'), 2)) | int(m.replace('X', '0'), 2)

mem = {}
with open('input') as f:
    for line in f:
        if line.startswith('mask'):
            m = line.strip().split()[2]
            continue
        addr, n = re.match(r'^mem\[(\d+)\] = (\d+)$', line).groups()
        mem[addr] = mask(int(n), m)
print(sum(mem.values()))

