#!/usr/bin/env python3

cups = '219748365'

cups = [int(c) for c in cups]

for i in range(100):
    cups.append(cups.pop(0))  # current is always last
    cur_cup = cups[-1]
    picked = cups[:3]
    cups = cups[3:]
    dest = (cur_cup - 2) % 9 + 1
    while dest not in cups:
        dest = (dest - 2) % 9 + 1
    dest_idx = cups.index(dest) + 1
    cups = cups[:dest_idx] + picked + cups[dest_idx:]

while cups[-1] != 1:
    cups.append(cups.pop(0))
print(''.join(map(str, cups[:-1])))

