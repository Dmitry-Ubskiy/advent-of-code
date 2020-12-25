#!/usr/bin/env python3

counts = 0
with open('input') as f:
    for p in f.read().split('\n\n'):
        p = set(p.replace('\n', ''))
        counts += len(p)
print(counts)
