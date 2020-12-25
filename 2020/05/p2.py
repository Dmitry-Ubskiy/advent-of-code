#!/usr/bin/env python3

def line2seat(line):
    row = int(line[:7].translate(str.maketrans('FB', '01')), base=2)
    col = int(line[7:10].translate(str.maketrans('LR', '01')), base=2)
    seat = row*8 + col
    return seat

with open('input') as f:
    seats = sorted(list(map(line2seat, f)))

i = 0
while i < len(seats)-1:
    if seats[i+1] == seats[i] + 2:
        print(seats[i]+1)
    i += 1
