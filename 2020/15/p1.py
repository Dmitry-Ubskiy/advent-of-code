#!/usr/bin/env python3

numbers = list(reversed([8,11,0,19,1,2]))
target = 2020

while len(numbers) < target:
    if numbers[0] in numbers[1:]:
        d = 1 + numbers[1:].index(numbers[0])
    else:
        d = 0
    numbers.insert(0, d)

print(numbers[0])

