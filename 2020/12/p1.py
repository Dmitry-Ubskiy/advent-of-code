#!/usr/bin/env python3

x, y = 0, 0

facing = 'E'
s = ['E', 'S', 'W', 'N']
with open('input') as f:
    for line in f:
        cmd, *n = line.strip()
        n = int(''.join(n))

        if cmd == 'F':
            cmd = facing

        if cmd == 'R':
            qs = n // 90  # quarter-turns
            idx = (s.index(facing) + qs) % 4
            facing = s[idx]
        elif cmd == 'L':
            qs = n // 90  # quarter-turns
            idx = (s.index(facing) - qs) % 4
            facing = s[idx]
        elif cmd == 'S':
            y += n
        elif cmd == 'N':
            y -= n
        elif cmd == 'E':
            x += n
        elif cmd == 'W':
            x -= n

print(abs(x) + abs(y))
