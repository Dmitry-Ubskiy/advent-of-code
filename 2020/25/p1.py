#!/usr/bin/env python3

def get_loop_size(target):
    value = 1
    loop_size = 0
    while True:
        loop_size += 1
        value = (value * 7) % 20201227
        if value == target:
            return loop_size

def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value

with open('input') as f:
    # either order ought to work
    card_pubkey, door_pubkey = map(int, f.read().split())

print(transform(door_pubkey, get_loop_size(card_pubkey)))
