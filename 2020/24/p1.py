#!/usr/bin/env python3

from collections import defaultdict


#     0,-1   +1,-1
#
# -1,0    q,r    +1,0
#
#    -1,+1   0,+1
def path_to_coords(p):
    i = 0
    q, r = 0, 0
    while i < len(p):
        if p[i] in 'ns':
            d = p[i:i+2]
            i += 2
        else:
            d = p[i]
            i += 1
        if d == 'e' or d == 'ne':
            q += 1
        if d == 'w' or d == 'sw':
            q -= 1
        if 'n' in d:
            r -= 1
        if 's' in d:
            r += 1
    return q, r


touched_tiles = defaultdict(lambda: False)
with open('input') as f:
    for line in f:
        coords = path_to_coords(line.strip())
        touched_tiles[coords] = not touched_tiles[coords]
print(sum(touched_tiles.values()))
