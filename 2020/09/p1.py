#!/usr/bin/env python3

def is_valid(n, prev):
    ps = sorted(prev)
    lo = 0
    hi = len(prev) - 1
    while lo < hi:
        while ps[lo] + ps[hi] > n:
            hi -= 1
            if hi <= lo:
                return False
        if ps[lo] + ps[hi] == n:
            return True
        lo += 1
    return False

with open('input') as f:
    prev = [int(f.readline()) for i in range(25)] # preamble
    for n in map(int, f):
        if not is_valid(n, prev):
            print(n)
        prev = prev[1:] + [n]

