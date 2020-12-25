#!/usr/bin/env python3

with open('input') as f:
    js = sorted(list(map(int, f)))

ds = {}
for p, n in zip([0] + js, js + [js[-1]+3]):
    ds.setdefault(n-p, 0)
    ds[n-p] += 1
print(ds[1] * ds[3])
