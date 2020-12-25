#!/usr/bin/env python3

def edges_hash(tile):
    edges = [
            min(int(s, 2), int(s[::-1], 2))
        for s in (
            ''.join(map(str, tile[0])),                     # N
            ''.join(map(str, (row[-1] for row in tile))),   # E
            ''.join(map(str, tile[-1])),                    # S
            ''.join(map(str, (row[0] for row in tile))),    # W
        )
    ]
    return edges


tiles = {}
with open('input') as f:
    for p in f.read().split('\n\n'):
        if not p.strip():
            continue
        head, *tile = p.strip().split('\n')
        idx = int(head[len('Tile '):-1])
        tile = [['.#'.index(c) for c in row] for row in tile]
        tiles[idx] = edges_hash(tile)

matching_edges = {}
for t, edges in tiles.items():
    for e in edges:
        matching_edges.setdefault(e, [])
        matching_edges[e].append(t)
matching_edges = {k: v for k,v in matching_edges.items() if len(v) == 2}  # assuming each match only affects 2 tiles with no false matches

# neighbors a tile needs to match with:
# 2 3 2
# 3 4 3
# 2 3 2
# if a tile has exactly 2 edges matching other tiles, it must be in a corner
# NOTE this is a MASSIVE assumption, but hey, it works for this
prod = 1
for t in tiles:
    if len(set(tiles[t]).intersection(matching_edges.keys())) == 2:  
        prod *= t
print(prod)
