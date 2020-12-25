#!/usr/bin/env python3

import re

def mask(n, m): 
    n |= int(m.replace('X', '0'), 2)
    def float(n, m):
        if 'X' not in m:
            yield n
            return
        i = len(m) - m.index('X') - 1
        m_ = m.replace('X', '0', 1)
        for x in float((1 << i) | n, m_):
            yield x
        for x in float(~(1 << i) & n, m_):
            yield x
    return float(n, m)

mem = {}
with open('input') as f:
    for line in f:
        if line.startswith('mask'):
            m = line.strip().split()[2]
            continue
        addr, n = re.match(r'^mem\[(\d+)\] = (\d+)$', line).groups()
        for a in mask(int(addr), m):
            mem[a] = int(n)
print(sum(mem.values()))

