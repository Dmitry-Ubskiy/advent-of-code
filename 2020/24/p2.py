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

max_days = 100
dv = [(dq, dr) for dq in (-1, 0, 1) for dr in (-1, 0, 1) if abs(dq+dr) < 2 and not (dq == dr == 0)]
for i in range(max_days):
    neighbors = {k: 0 for k in touched_tiles}
    for (q, r), is_black in touched_tiles.items():
        if not is_black:
            continue
        for dq, dr in dv:
            adj = (q+dq, r+dr)
            neighbors.setdefault(adj, 0)
            neighbors[adj] += 1
    for coords, black_neighbors in neighbors.items():
        if not touched_tiles[coords] and black_neighbors == 2:
            touched_tiles[coords] = True
        elif touched_tiles[coords] and (black_neighbors == 0 or black_neighbors > 2):
            touched_tiles[coords] = False

print(sum(touched_tiles.values()))

