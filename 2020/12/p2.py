#!/usr/bin/env python3

x, y = 0, 0
dx, dy = 10, -1

with open('input') as f:
    for line in f:
        cmd, *n = line.strip()
        n = int(''.join(n))

        if cmd == 'F':
            x += n * dx
            y += n * dy
        elif cmd == 'R':
            qs = n // 90  # quarter-turns
            for i in range(qs):
                dx, dy = -dy, dx
        elif cmd == 'L':
            qs = n // 90  # quarter-turns
            for i in range(qs):
                dx, dy = dy, -dx
        elif cmd == 'S':
            dy += n
        elif cmd == 'N':
            dy -= n
        elif cmd == 'E':
            dx += n
        elif cmd == 'W':
            dx -= n

print(abs(x) + abs(y))
