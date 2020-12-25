#!/usr/bin/env python3

trees = 0
with open('input') as f:
    x = 0
    for line in f:
        if line[x] == '#':
            trees += 1
        w = len(line.strip())
        x = (x + 3) % w
print(trees)
