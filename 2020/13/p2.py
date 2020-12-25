#!/usr/bin/env python3

from math import prod

with open('input') as f:
    f.readline()
    buses = [int(b) if b != 'x' else None for b in f.readline().strip().split(',')]

n = 1
b = buses[0]
t = 0

while n < len(buses):
    while all((t + i) % x == 0 for i, x in enumerate(buses[:n+1]) if x is not None):
        n += 1
        if n == len(buses):
            print(t)
            exit(0)
    t += prod(x for x in buses[:n] if x is not None)

