#!/usr/bin/env python3

with open('input') as f:
    a = set(map(int, f.readlines()))

for n in a:
    if 2020-n in a:
        print(n*(2020-n))
        break
