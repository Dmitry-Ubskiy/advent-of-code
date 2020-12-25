#!/usr/bin/env python3

def in_drange(x, dr):
    s1, e1, s2, e2 = dr
    if s1 <= x <= e1 or s2 <= x <= e2:
        return True
    return False

state = 'rules'
rules = {}

your_ticket = None
tickets = []

with open('input') as f:
    for line in f:
        line = line.strip()
        if not line:
            state = ''
            continue
        if state == '':
            state = line[:-1]
        elif state == 'rules':
            name, ranges = line.split(':')
            ranges = ranges.strip().split()
            s1, e1 = map(int, ranges[0].split('-'))
            s2, e2 = map(int, ranges[2].split('-'))
            rules[name] = (s1, e1, s2, e2)
        elif 'ticket' in state:
            fields = list(map(int, line.split(',')))
            if state == 'your ticket':
                assert your_ticket is None
                your_ticket = fields
            else:
                if any(not any(in_drange(f, dr) for dr in rules.values()) for f in fields):
                    continue
                tickets.append(fields)

possibilities = [list(rules.keys()) for _ in your_ticket]
for t in (your_ticket, *tickets):
    for i, f in enumerate(t):
        possibilities[i] = [r for r in possibilities[i] if in_drange(f, rules[r])]
while any(len(s) > 1 for s in possibilities):
    fixed = [s[0] for s in possibilities if len(s) == 1]
    possibilities = [s if len(s) == 1 else [r for r in s if r not in fixed] for s in possibilities]
field_names = sum(possibilities, [])
prod = 1
for n, f in zip(field_names, your_ticket):
    if n.startswith('departure'):
        prod *= f
print(prod)
