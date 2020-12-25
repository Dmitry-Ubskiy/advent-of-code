#!/usr/bin/env python3

import numpy as np

with open('input') as f:
    cube = [[[1 if c == '#' else 0 for c in s.strip()] for s in f.readlines()]]

def trim_zeros(arr):
    slices = [slice(None)] * arr.ndim
    for dim in range(arr.ndim):
        slices[dim] = 0
        while not np.any(arr[tuple(slices)]):
            slices[dim] += 1
        start = slices[dim]

        slices[dim] = -1
        while not np.any(arr[tuple(slices)]):
            slices[dim] -= 1
        finish = slices[dim] + 1
        if finish >= 0:
            finish = None

        slices[dim] = slice(start, finish)
    return arr[tuple(slices)]

def convolve_3d(cube):
    padded = np.pad(cube, 2, 'constant')
    depth, height, width = padded.shape

    slices_1d = [slice(0, -2), slice(1, -1), slice(2, None)]
    slices_3d = [
        (slices_1d[dz], slices_1d[dy], slices_1d[dx])
        for dx in (0, 1, 2) for dy in (0, 1, 2) for dz in (0, 1, 2)
        if not (dx == dy == dz == 1)
    ]

    neighbors = sum((padded[s] for s in slices_3d))
    new_cube = np.logical_or(neighbors == 3, neighbors + padded[1:-1,1:-1,1:-1] == 3).astype(int)
    return trim_zeros(new_cube)

max_iter = 6
for _ in range(max_iter):
    cube = convolve_3d(cube)
print(np.sum(cube))
