from parse import parse_lines
import numpy as np

grid = np.array([[char for char in line] for line in parse_lines()])
energy = np.zeros(grid.shape)
rows, columns = grid.shape
traveled = set()
reflections = {
    "|": {
        (0, 1): [(1, 0), (-1, 0)],
        (0, -1): [(1, 0), (-1, 0)],
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
    },
    "-": {
        (1, 0): [(0, 1), (0, -1)],
        (-1, 0): [(0, 1), (0, -1)],
        (0, 1): [(0, 1)],
        (0, -1): [(0, -1)],
    },
    "/": {(0, 1): [(-1, 0)], (0, -1): [(1, 0)], (1, 0): [(0, -1)], (-1, 0): [(0, 1)]},
    "\\": {(0, 1): [(1, 0)], (0, -1): [(-1, 0)], (1, 0): [(0, 1)], (-1, 0): [(0, -1)]},
    ".": {(0, 1): [(0, 1)], (0, -1): [(0, -1)], (1, 0): [(1, 0)], (-1, 0): [(-1, 0)]},
}


def add(a, b):
    r1, c1 = a
    r2, c2 = b
    return r1 + r2, c1 + c2


def within_grid(node):
    r, c = node
    return 0 <= r < rows and 0 <= c < columns


def find_next_trajectories(node, direction):
    if within_grid(node):
        energy[node] += 1
        symbol = grid[node]
        traveled.add((node, direction))
        return [
            (add(node, new_direction), new_direction)
            for new_direction in reflections[symbol][direction]
            if (add(node, new_direction), new_direction) not in traveled
        ]
    else:
        return []


def traverse_beam(node, direction):
    trajectories = [(node, direction)]
    while trajectories:
        node, direction = trajectories.pop()
        trajectories.extend(find_next_trajectories(node, direction))


traverse_beam((0, 0), (0, 1))
print(np.count_nonzero(energy > 0))
