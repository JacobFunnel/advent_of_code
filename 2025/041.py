from parse import parse_lines

grid = {
    r + c * 1j
    for r, line in enumerate(parse_lines())
    for c, char in enumerate(line)
    if char == "@"
}


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


print(sum(1 for point in grid if len(neighbors(point).intersection(grid)) < 4))
