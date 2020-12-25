#!/usr/bin/env python3

with open('input') as f:
    program = [
        (cmd, int(n))
        for cmd, n in
        [line.strip().split() for line in f]
    ]

pc = 0
acc = 0
visited = set()
while pc not in visited:
    visited.add(pc)
    cmd, n = program[pc]
    if cmd == 'jmp':
        pc += n
        continue
    if cmd == 'acc':
        acc += n
    pc += 1
print(acc)
