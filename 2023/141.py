import numpy as np
from parse import parse_lines

grid = np.array([[char for char in line] for line in parse_lines()])
# print(grid)
wall_indices = list((r, c) for r, c in zip(*np.where(grid == "#")))

rows, columns = grid.shape
column_indices = set(range(columns))


def range_chunk(indices):
    range_indices = []
    while indices:
        current = indices.pop(0)
        if not range_indices:
            range_indices += [current]
        else:
            if not current == previous + 1:
                range_indices += [previous, current]
        previous = current
    if len(range_indices) % 2:
        range_indices += [previous]
    return [(range_indices[idx], range_indices[idx + 1]) for idx in range(0, len(range_indices), 2)]


for col in range(columns):
    walls = set(np.where(grid[:, col] == "#")[0])
    non_walls = column_indices - walls
    for a, b in range_chunk(sorted(non_walls)):
        grid[a : b + 1, col] = np.sort(grid[a : b + 1, col])[::-1]

total = 0
for idx, row in enumerate(grid):
    total += len(np.where(row == "O")[0]) * (columns - idx)
print(total)
