from time import sleep
import numpy

with open("input/14.txt", "r") as f:
    line_coords = [
        [tuple(map(int, pair.split(","))) for pair in row.split(" -> ")]
        for row in f.read().splitlines()
    ]


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
    try:
        if grid[y + 1, x] == ".":
            sand_fall((x, y + 1))
        elif grid[y + 1, x - 1] == ".":
            sand_fall((x - 1, y + 1))
        elif grid[y + 1, x + 1] == ".":
            sand_fall((x + 1, y + 1))
        else:
            grid[y, x] = "o"
    except IndexError:
        print(numpy.count_nonzero(grid == "o"))
        done = True


rocks = set()
source = (500, 0)
done = False
for line in line_coords:
    for i in range(len(line) - 1):
        rocks |= interpolation(line[i], line[i + 1])
xmin = min(rocks | {source}, key=lambda coord: coord[0])[0]
xmax = max(rocks | {source}, key=lambda coord: coord[0])[0]
ymin = min(rocks | {source}, key=lambda coord: coord[1])[1]
ymax = max(rocks | {source}, key=lambda coord: coord[1])[1]
grid = numpy.full((ymax - ymin + 1, xmax - xmin + 1), ".")
for thing in rocks | {source}:
    x, y = thing
    grid[y - ymin, x - xmin] = "#" if thing not in {source} else "+"
print("".join("".join(line) + "\n" for line in grid))

while not done:
    sand_fall(add(source, (-xmin, -ymin)))
