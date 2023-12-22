import numpy as np

with open("../input/day13_input.txt", "r") as f:
    in_put = [tuple(line.strip().split(",")) for line in f.readlines()]


x_coord, y_coord = set(), set()
dots, folds = [], []

for entry in in_put:
    if len(entry) == 2:
        x, y = int(entry[0]), int(entry[1])
        dots.append((x, y))
        x_coord.add(x)
        y_coord.add(y)
    else:
        folds.append(entry[0][11:].split("="))

folds.pop(0)
rows, columns = max(x_coord) + 1, max(y_coord) + 1
grid = np.zeros(shape=(rows, columns), dtype=int)
grid[tuple(zip(*dots))] = 1

for i in range(len(folds)):
    axis, value = folds[i]
    value = int(value)
    rows, columns = np.shape(grid)
    if axis == "x":
        for step in range(1, rows - value):
            for column in range(columns):
                grid[value - step, column] += grid[value + step, column]
        grid = np.delete(grid, range(value + 1, rows), axis=0)
    else:
        for step in range(1, columns - value):
            for row in range(rows):
                grid[row, value - step] += grid[row, value + step]
        grid = np.delete(grid, range(value + 1, columns), axis=1)

print(np.where(grid > 0, 1, grid))  # PZFJHRFZ
