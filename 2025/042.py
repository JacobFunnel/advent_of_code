from parse import parse_lines

grid = {
    r + c * 1j
    for r, line in enumerate(parse_lines())
    for c, char in enumerate(line)
    if char == "@"
}
points_removed = 0


def neighbors(point):
    return {
        point + 1,
        point - 1,
        point + 1j,
        point - 1j,
        point + 1 + 1j,
        point - 1 + 1j,
        point + 1 - 1j,
        point - 1 - 1j,
    }


def points_to_remove(grid):
    return {point for point in grid if len(neighbors(point).intersection(grid)) < 4}


while points := points_to_remove(grid):
    grid -= points
    points_removed += len(points)

print(points_removed)
