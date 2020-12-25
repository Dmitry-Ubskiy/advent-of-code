#!/usr/bin/env python3

with open('input') as f:
    area = list(map(list, map(str.strip, f.readlines())))

h = len(area)
w = len(area[0])

vs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def next_area():
    counts = [[0] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if area[y][x] != '#':
                continue
            for dx, dy in vs:
                sx, sy = x + dx, y + dy
                while 0 <= sx < w and 0 <= sy < h:
                    if area[sy][sx] in 'L#':
                        counts[sy][sx] += 'L#'.index(area[y][x])
                        break
                    sx += dx
                    sy += dy

    n_area = [r[:] for r in area]
    for y in range(h):
        for x in range(w):
            if counts[y][x] == 0 and area[y][x] == 'L':
                n_area[y][x] = '#'
            if counts[y][x] >= 5 and area[y][x] == '#':
                n_area[y][x] = 'L'
    return n_area

na = next_area()
while area != na:
    area = na
    na = next_area()
print(sum(r.count('#') for r in area))
