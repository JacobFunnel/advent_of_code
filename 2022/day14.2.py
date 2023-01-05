from time import sleep
import numpy

with open("input/14.txt", "r") as f:
    line_coords = [[tuple(map(int, pair.split(","))) for pair in row.split(" -> ")]
                   for row in f.read().splitlines()]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def interpolation(a, b):
    points = {a, b}
    x1, y1 = a
    x2, y2 = b
    dx = x2 - x1
    dy = y2 - y1
    mx = int(abs(dx) / (dx or 1))
    my = int(abs(dy) / (dy or 1))
    for n in range(1, abs(dx or dy)):
        points |= {add(a, (n * mx, n * my))}
    return points


def sand_fall(point):
    global grid, done
    x, y = point
    if grid[y + 1, x] in [".", "+"]:
        sand_fall((x, y + 1))
    elif grid[y + 1, x - 1] in [".", "+"]:
        sand_fall((x - 1, y + 1))
    elif grid[y + 1, x + 1] in [".", "+"]:
        sand_fall((x + 1, y + 1))
    else:
        grid[y, x] = "o"
        if grid[source[::-1]] == "o":
            done = True
            print(numpy.count_nonzero(grid == "o"))


rocks = set()
source = (500, 0)
done = False
for line in line_coords:
    for i in range(len(line) - 1):
        rocks |= interpolation(line[i], line[i + 1])
xmax = max(rocks | {source}, key=lambda coord: coord[0])[0]
ymax = max(rocks | {source}, key=lambda coord: coord[1])[1]
# double grid size on the x-axis to allow for the overflow
grid = numpy.full((ymax + 2 + 1, 2 * xmax + 1), ".")
for rock in rocks:
    x, y = rock
    grid[y, x] = "#"
grid[source[::-1]] = "+"
grid[-1] = "#"  # Floor is rock

while not done:
    sand_fall(add(source, (0, -1)))  # Start dropping sand 1 y-unit higher up

