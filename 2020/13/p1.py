#!/usr/bin/env python3

with open('input') as f:
    t = int(f.readline())
    buses = [int(b) for b in f.readline().strip().split(',') if b != 'x']

b = min(buses, key=lambda x: x - (t % x))
print(b * (b - (t%b)))
