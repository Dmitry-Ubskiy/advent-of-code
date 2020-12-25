#!/usr/bin/env python3

import re

parser = re.compile(r'([a-z]+ [a-z]+) bags?')

tree = {}
with open('input') as f:
    for line in f:
        outer, *inner = parser.findall(line.strip())
        if inner[0] == 'no other':
            tree[outer] = []
            continue
        tree[outer] = inner

count = 0
target = 'shiny gold'
memo = {}
def has_target(outer):
    for k in tree[outer]:
        if k in memo and memo[k]:
            memo[outer] = True
            break
        if k == target or has_target(k):
            memo[outer] = True
            break
    if outer not in memo:
        memo[outer] = False
    return memo[outer]

for k in tree:
    if has_target(k):
        count += 1
print(count)
