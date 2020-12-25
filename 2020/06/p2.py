#!/usr/bin/env python3

counts = 0
with open('input') as f:
    for p in f.read().split('\n\n'):
        answers = list(map(set, p.split()))
        counts += len(set.intersection(*answers))
print(counts)
