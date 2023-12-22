import numpy as np
from math import prod
from parse import parse_lines

patterns = parse_lines(2)
grids = [
    (np.array([[char for char in line] for line in pattern.split("\n")])) for pattern in patterns
]
total = 0
mult_map = {0: 100, 1: 1}
for grid in grids:
    for axis, length in enumerate(grid.shape):
        for idx in range(1, length):
            dist = min(len(range(idx)), length - idx)
            mirror = np.take(grid, list(range(idx - dist, idx)), axis=axis)
            reflection = np.flip(np.take(grid, list(range(idx, idx + dist)), axis=axis), axis=axis)
            if prod(mirror.shape) - np.count_nonzero(mirror == reflection) == 1:
                total += mult_map[axis] * idx

print(total)
