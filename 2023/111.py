from itertools import combinations

from parse import parse_lines


def expand_grid(grid):
    grid = expand_rows(grid)
    transposed = list(map(list, zip(*grid)))
    transposed = expand_rows(transposed)
    grid = list(map(list, zip(*transposed)))
    return grid


def expand_rows(grid):
    expanded_grid = []
    for row in grid:
        expanded_grid.append(row)
        if all(char == "." for char in row):
            expanded_grid.append(row)
    return expanded_grid


grid = expand_grid(parse_lines())
galaxies = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "#"]
total = 0
for (g1r, g1c), (g2r, g2c) in combinations(galaxies, 2):
    total += abs(g2r - g1r) + abs(g2c - g1c)
print(total)
