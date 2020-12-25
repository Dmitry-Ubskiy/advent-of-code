#!/usr/bin/env python3

with open('input') as f:
    numbers = list(map(int, f))

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

prev = numbers[:25] # preamble
for n in numbers[25:]:
    if not is_valid(n, prev):
        weakness = n
        break
    prev = prev[1:] + [n]

lo = 0
hi = 0  # non-inclusive

s = 0
while s != n:
    if s < n:
        s += numbers[hi]
        hi += 1
    elif s > n:
        s -= numbers[lo]
        lo += 1

print(min(numbers[lo:hi]) + max(numbers[lo:hi]))
