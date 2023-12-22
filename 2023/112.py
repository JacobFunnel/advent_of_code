from itertools import combinations

import numpy as np

from parse import parse_lines

grid = np.array([[char for char in line] for line in parse_lines()])
galaxies = list((a, b) for a, b in zip(*np.where(grid == "#")))
expansion_rows = [r for r, row in enumerate(grid) if all(char == "." for char in row)]
expansion_cols = [c for c, col in enumerate(grid.T) if all(char == "." for char in col)]
h_expansion = np.ones(grid.shape)
v_expansion = np.ones(grid.shape)
for r in expansion_rows:
    v_expansion[r, :] = 1000000
for c in expansion_cols:
    h_expansion[:, c] = 1000000


def spacewalk(n1, n2):
    steps = 0
    r1, c1 = n1
    r2, c2 = n2
    dr = r2 - r1
    if dr:
        step_r = int(dr / abs(dr))
        r_indices = list(range(r1 + step_r, r2 + step_r, step_r))
        c_indices = [c1] * len(r_indices)
        steps += sum(v_expansion[r_indices, c_indices])

    dc = c2 - c1
    if dc:
        step_c = int(dc / abs(dc))
        c_indices = list(range(c1 + step_c, c2 + step_c, step_c))
        r_indices = [r2] * len(c_indices)
        steps += sum(h_expansion[r_indices, c_indices])
    return steps


total = 0
for g1, g2 in combinations(galaxies, 2):
    total += spacewalk(g1, g2)

print(int(total))
