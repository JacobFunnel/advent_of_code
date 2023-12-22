import numpy as np

with open("../input/day13_input.txt", "r") as f:
    in_put = [tuple(line.strip().split(",")) for line in f.readlines()]

dots = []
x_coord = set()
y_coord = set()
folds = []

for entry in in_put:
    if len(entry) == 2:
        x, y = int(entry[0]), int(entry[1])
        dots.append((x, y))
        x_coord.add(x)
        y_coord.add(y)
    else:
        folds.append(entry[0][11:].split("="))

rows, columns = max(x_coord) + 1, max(y_coord) + 1
folds.pop(0)
grid = np.zeros(shape=(rows, columns), dtype=int)
grid[tuple(zip(*dots))] = 1
print(len(grid[grid > 0]))

for i in range(1):
    axis, value = folds[i]
    value = int(value)

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
    print(len(grid[grid > 0]))
