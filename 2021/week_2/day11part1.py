import numpy as np

with open('../input/day11_input.txt', 'r') as f:
    grid = np.mat([[int(char) for char in line.strip()] for line in f.readlines()])

rows, columns = np.shape(grid)
all_nodes = set()
number_of_flashes = 0

for x in range(rows):
    for y in range(columns):
        all_nodes.add((x, y))


def neighbors(node):
    directions = {(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)}
    result = set()
    for direction in directions:
        neighbor = (node[0] + direction[0], node[1] + direction[1])
        if neighbor in all_nodes:
            result.add(neighbor)
    return result


def flash(will_flash):
    global grid
    has_flashed = set()
    while len(will_flash):
        for node in will_flash:
            adjecent = neighbors(node)
            for neighbor in adjecent:
                grid[neighbor] += 1
            has_flashed.add(node)
        will_flash = set(map(tuple, np.argwhere(grid > 9))) - has_flashed


def take_step():
    global grid, number_of_flashes
    grid += 1
    will_flash = set(map(tuple, np.argwhere(grid > 9)))
    flash(will_flash)
    number_of_flashes += len(np.argwhere(grid > 9))
    grid = np.where(grid > 9, 0, grid)


for i in range(100):
    take_step()

print(number_of_flashes)
