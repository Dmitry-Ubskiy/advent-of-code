#!/usr/bin/env python3

def line2seat(line):
    row = int(line[:7].translate(str.maketrans('FB', '01')), base=2)
    col = int(line[7:10].translate(str.maketrans('LR', '01')), base=2)
    return row*8 + col

with open('input') as f:
    print(max(map(line2seat, f)))
