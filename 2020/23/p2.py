#!/usr/bin/env python3

cups = '219748365'

max_iter = 10_000_000
n_cups = 1_000_000

cups = [int(c) - 1 for c in cups]
cups.extend(range(max(cups) + 1, n_cups))
assert len(cups) == n_cups

# next cup; abbreviated
n = {p: n for p, n in zip(cups, cups[1:] + cups[:1])}
n = [n[i] for i in range(n_cups)]

current = cups[0]
for i in range(max_iter):
    picked_begin = n[current]
    picked_mid = n[picked_begin]
    picked_end = n[picked_mid]

    picked = (picked_begin, picked_mid, picked_end)

    n[current] = n[picked_end]
    dest = (current - 1) % n_cups
    while dest in picked:
        dest = (dest - 1) % n_cups

    n[picked_end] = n[dest]
    n[dest] = picked_begin

    current = n[current]

print((n[0] + 1) * (n[n[0]] + 1))
