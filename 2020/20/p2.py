#!/usr/bin/env python3

import numpy as np


def edges_hash(tile):
    edges = {
        d: min(int(s, 2), int(s[::-1], 2))
        for d, s in (
            ('N', ''.join(map(str, tile[0]))),
            ('E', ''.join(map(str, (row[-1] for row in tile)))),
            ('S', ''.join(map(str, tile[-1]))),
            ('W', ''.join(map(str, (row[0] for row in tile)))),
        )
    }
    return edges


monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
]


tiles = {}
tile_edges = {}


def vflip(tile):
    tiles[tile] = tiles[tile][::-1]
    tile_edges[tile]['N'], tile_edges[tile]['S'] = tile_edges[tile]['S'], tile_edges[tile]['N']


def hflip(tile):
    tiles[tile] = [row[::-1] for row in tiles[tile]]
    tile_edges[tile]['E'], tile_edges[tile]['W'] = tile_edges[tile]['W'], tile_edges[tile]['E']


def rotate(tile, start, end):
    if start == end:
        return
    if set((start, end)) in ({'N', 'S'}, {'W', 'E'}):
        # equivalent
        vflip(tile)
        hflip(tile)
    else:  # quarter turn
        d = 'NESW'.index(start) - 'NESW'.index(end)
        if abs(d) == 3:  # N->W or W->N
            d = -d/3
        tiles[tile] = np.rot90(tiles[tile], k=d)
        if d == -1:  # CW
            tile_edges[tile]['N'], tile_edges[tile]['E'], tile_edges[tile]['S'], tile_edges[tile]['W'] = \
                tile_edges[tile]['W'], tile_edges[tile]['N'], tile_edges[tile]['E'], tile_edges[tile]['S']
        else:  # CCW
            tile_edges[tile]['N'], tile_edges[tile]['E'], tile_edges[tile]['S'], tile_edges[tile]['W'] = \
                tile_edges[tile]['E'], tile_edges[tile]['S'], tile_edges[tile]['W'], tile_edges[tile]['N']


def remove_sea_monster(arr, win):
    ah, aw = np.shape(arr)
    wh, ww = np.shape(win)
    for y in range(ah - wh + 1):
        for x in range(aw - ww + 1):
            padded_win = np.pad(win, ((y, ah - wh - y), (x, aw - ww - x)))
            assert padded_win.shape == arr.shape
            if np.sum(win) == np.sum(padded_win * arr):
                arr -= padded_win
    return arr


if __name__ == '__main__':
    with open('input') as f:
        for p in f.read().split('\n\n'):
            if not p.strip():
                continue
            head, *tile = p.strip().split('\n')

            idx = int(head[len('Tile '):-1])

            tile = [['.#'.index(c) for c in row] for row in tile]
            tile_edges[idx] = edges_hash(tile)

            trimmed_tile = [row[1:-1] for row in tile[1:-1]]
            tiles[idx] = trimmed_tile

    matching_edges = {}
    for t, edges in tile_edges.items():
        for e in edges.values():
            matching_edges.setdefault(e, [])
            matching_edges[e].append(t)
    matching_edges = {k: v for k,v in matching_edges.items() if len(v) == 2}  # assuming each match only affects 2 tiles with no false matches

    # neighbors a tile needs to match with:
    # 2 3 2
    # 3 4 3
    # 2 3 2
    # if a tile has exactly 2 edges matching other tiles, it must be in a corner
    # NOTE this is a MASSIVE assumption, but hey, it works for this
    corners = [
        t for t in tiles
        if len(set(tile_edges[t].values()).intersection(matching_edges.keys())) == 2
    ]

    # we know the image is square
    map_dim = int(len(tiles) ** .5)

    topleft = corners[0]  # any corner works
    tile_map = [[] for _ in range(map_dim)]
    tile_map[0].append(topleft)

    if tile_edges[topleft]['E'] not in matching_edges:
        hflip(topleft)
    if tile_edges[topleft]['S'] not in matching_edges:
        vflip(topleft)

    for x in range(1, map_dim):  # top border
        left = tile_map[0][x-1]

        glue_edge = tile_edges[left]['E']
        next_tile = [t for t in matching_edges[glue_edge] if t != left][0]
        glue_edge_idx = [k for k, v in tile_edges[next_tile].items() if v == glue_edge][0]

        rotate(next_tile, glue_edge_idx, 'W')
        if tile_edges[next_tile]['S'] not in matching_edges:
            vflip(next_tile)
        tile_map[0].append(next_tile)

    for y in range(1, map_dim):
        for x in range(map_dim):
            top = tile_map[y-1][x]
            glue_edge = tile_edges[top]['S']
            next_tile = [t for t in matching_edges[glue_edge] if t != top][0]
            glue_edge_idx = [k for k, v in tile_edges[next_tile].items() if v == glue_edge][0]

            rotate(next_tile, glue_edge_idx, 'N')
            if x == 0:
                if tile_edges[next_tile]['E'] not in matching_edges:
                    hflip(next_tile)
            else:
                if tile_edges[tile_map[y][x-1]]['E'] != tile_edges[next_tile]['W']:
                    hflip(next_tile)
            tile_map[y].append(next_tile)

    map_pic = np.vstack([np.hstack(list(map(tiles.__getitem__, r))) for r in tile_map])
    # print('\n'.join(''.join(map('.# '.__getitem__, r)) for r in map_pic))  # <-- prints cool map

    monster_win = [[' #'.index(c) for c in r] for r in monster]

    hashes = np.sum(map_pic)
    # assume sea monsters never occupy the same char
    for flip in range(2):
        for i in range(4):
            map_pic = remove_sea_monster(map_pic, monster_win)
            if np.sum(map_pic) != hashes:
                print(np.sum(map_pic))
                exit(0)
            map_pic = np.rot90(map_pic)
        map_pic = np.flipud(map_pic)

