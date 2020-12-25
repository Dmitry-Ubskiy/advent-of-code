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

error_rate = 0
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
                for f in fields:
                    if not any([in_drange(f, dr) for dr in rules.values()]):
                        error_rate += f
                tickets.append(fields)

print(error_rate)
