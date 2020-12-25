#!/usr/bin/env python3

import re

rules = {}

def match_chain(message, chain):
    leftovers = [message]
    for rule in chain:
        leftovers = sum([match(b, rule) for b in leftovers], [])
        if not leftovers:
            return []
    return leftovers


def match(message, rule='0'):
    if type(rules[rule]) == str:
        if message.startswith(rules[rule]):
            return [message[1:]]
        else:
            return []

    leftovers = sum([match_chain(message, chain) for chain in rules[rule]], [])
    return leftovers


count = 0
with open('input.p2') as f:
    in_rules = True
    for line in f:
        line = line.strip()
        if not line:
            in_rules = False
            continue
        if in_rules:
            if '"' in line:
                n, ch, _ = re.split(r'[: "]+', line)
                rules[n] = ch
            else:
                n, *subrules = re.split(r'(?: *[:|]+ *)', line)
                rules[n] = [s.split() for s in subrules]
        else:  # messages
            if '' in match(line):
                count += 1
print(count)
