#!/usr/bin/env python3

with open('input') as f:
    a = sorted(map(int, f.readlines()))

lo = 0
hi = len(a) - 1

while lo < hi:
    while a[lo] + a[hi] >= 2020:
        hi -= 1
    c = 2020 - a[lo] - a[hi]
    if c in a:
        print(c*a[lo]*a[hi])
        break
    lo += 1

