#!/usr/bin/env python3

import re

parser = re.compile(r'(\d+ )?([a-z]+ [a-z]+) bags?')

tree = {}
with open('input') as f:
    for line in f:
        (_, outer), *inner = parser.findall(line.strip())
        if inner[0][1] == 'no other':
            tree[outer] = []
            continue
        tree[outer] = list(map(lambda x: (int(x[0].strip()), x[1]), inner))

target = 'shiny gold'
memo = {}
def contents(c):
    if c in memo:
        return memo[c]
    count = 0
    for n, clr in tree[c]:
        count += n * (1 + contents(clr))
    memo[c] = count
    return memo[c]
print(contents(target))
