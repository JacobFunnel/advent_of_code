import numpy as np

from parse import parse_lines

patterns = parse_lines(2)
grids = [
    (np.array([[char for char in line] for line in pattern.split("\n")])) for pattern in patterns
]
total = 0
mult = {0: 100, 1: 1}
for grid in grids:
    for axis, length in enumerate(grid.shape):
        for idx in range(1, length):
            dist = min(len(range(idx)), length - idx)
            mirror = np.take(grid, list(range(idx - dist, idx)), axis=axis)
            reflection = np.flip(np.take(grid, list(range(idx, idx + dist)), axis=axis), axis=axis)
            if np.array_equal(mirror, reflection):
                total += mult[axis] * idx

print(total)
