#!/usr/bin/env python3

start = [8,11,0,19,1,2]
target = 30_000_000

n = start[-1]
t = len(start) - 1
last_enc = {n: i for i, n in enumerate(start[:-1])}
for i in range(target - len(start)):
    if n not in last_enc:
        next_n = 0
    else:
        next_n = t - last_enc[n]
    last_enc[n] = t
    t += 1
    n = next_n

print(n)

