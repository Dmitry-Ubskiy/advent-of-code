#!/usr/bin/env python3

with open('input') as f:
    program = [
        (cmd, int(n))
        for cmd, n in
        [line.strip().split() for line in f]
    ]

def diverge(pc_, acc_, v_):
    visited = {x for x in v_}
    cmd, n = program[pc_]
    acc = acc_
    if cmd == 'nop':
        pc = pc_ + n
    else:
        pc = pc_ + 1
    while pc not in visited:
        if pc >= len(program):
            print(acc)
            exit(0)  # we're done!
        visited.add(pc)
        cmd, n = program[pc]
        if cmd == 'acc':
            acc += n
        if cmd == 'jmp':
            pc += n
            continue
        pc += 1

pc = 0
acc = 0
visited = set()
while pc not in visited:
    visited.add(pc)
    cmd, n = program[pc]
    if cmd == 'acc':
        acc += n
    diverge(pc, acc, visited)
    if cmd == 'jmp':
        pc += n
        continue
    pc += 1

