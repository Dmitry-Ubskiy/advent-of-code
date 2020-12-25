#!/usr/bin/env python3

with open('input') as f:
    area = list(map(list, map(str.strip, f.readlines())))

h = len(area)
w = len(area[0])

def next_area():
    counts = [[0] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if area[y][x] != '#':
                continue
            for dy in (-1, 0, 1):
                cy = y + dy
                if cy < 0 or cy >= h:
                    continue
                for dx in (-1, 0, 1):
                    cx = x + dx
                    if cx < 0 or cx >= w:
                        continue
                    if dx == dy and dx == 0:
                        continue
                    counts[cy][cx] += 1
    n_area = [r[:] for r in area]
    for y in range(h):
        for x in range(w):
            if counts[y][x] == 0 and area[y][x] == 'L':
                n_area[y][x] = '#'
            if counts[y][x] >= 4 and area[y][x] == '#':
                n_area[y][x] = 'L'
    return n_area

na = next_area()
while area != na:
    area = na
    na = next_area()
print(sum(r.count('#') for r in area))
