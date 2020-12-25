#!/usr/bin/env python3

with open('input') as f:
    js = sorted(list(map(int, f)))

memo = {}
def count_paths(a, s=0):
    if len(a) == 0:
        return 1
    if (s, a[0]) in memo:
        return memo[(s, a[0])]
    count = 0
    for i, n in enumerate(a):
        if n > s+3:
            break
        count += count_paths(a[i+1:], n)
    memo[(s, a[0])] = count
    return memo[(s, a[0])]

print(count_paths(js))
