#!/usr/bin/env python3

from math import prod

vs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = {v: 0 for v in vs}
with open('input') as f:
    xs = [0] * 5
    ys = [0] * 5
    for h, line in enumerate(f):
        for i, (x, y, v) in enumerate(list(zip(xs, ys, vs))):
            if y == h:
                if line[x] == '#':
                    trees[v] += 1
                w = len(line.strip())
                xs[i] = (x + v[0]) % w
                ys[i] = y + v[1]

print(prod(trees.values()))
