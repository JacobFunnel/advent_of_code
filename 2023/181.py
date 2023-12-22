import numpy as np
import re
from parse import parse_lines


traversed_nodes = set()
offset = None
directions = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}


def parse():
    return [
        (udlr, int(amount), color)
        for udlr, amount, color in [line.split() for line in parse_lines()]
    ]


def add(a, b):
    r1, c1 = a
    r2, c2 = b
    return r1 + r2, c1 + c2


def mult(n, a):
    r, c = a
    return n * r, n * c


def dig(node, direction, amount):
    global traversed_nodes
    next_nodes = [add(node, mult(n, direction)) for n in range(amount + 1)]
    traversed_nodes |= set(next_nodes)
    return next_nodes[-1]


def traverse(instructions):
    node = (0, 0)
    for uplr, amount, _ in instructions:
        node = dig(node, directions[uplr], amount)


def create_grid():
    global offset
    min_row = min((node for node in traversed_nodes), key=lambda n: n[0])[0]
    max_row = max((node for node in traversed_nodes), key=lambda n: n[0])[0]
    min_column = min((node for node in traversed_nodes), key=lambda n: n[1])[1]
    max_column = max((node for node in traversed_nodes), key=lambda n: n[1])[1]
    rows = max_row - min_row + 1
    columns = max_column - min_column + 1
    offset = (-min_row, -min_column)
    grid = np.zeros((rows, columns))
    for node in traversed_nodes:
        grid[add(node, offset)] = 1
    return grid


def find_point_within_loop():
    for node in traversed_nodes:
        for neighbor in (add(add(node, offset), d) for d in directions.values()):
            if grid[neighbor] == 0 and within_loop(neighbor):
                return neighbor


def within_loop(point):
    r, c = point
    lines_of_sight = [grid[0 : r + 1, c], grid[r:, c], grid[r, 0 : c + 1], grid[r, c:]]
    for line in lines_of_sight:
        crossings = re.findall(r"[^.]+", "".join("." if n == 0 else "#" for n in line))
        if all(len(x) == 1 for x in crossings):
            return len(crossings) % 2 == 1


def floodfill(from_point):
    global grid
    points_to_flood_from = [from_point]
    while points_to_flood_from:
        node = points_to_flood_from.pop(0)
        for neighbor in (add(node, d) for d in directions.values()):
            if grid[neighbor] == 0:
                grid[neighbor] = 1
                points_to_flood_from.append(neighbor)


def print_grid():
    for row in grid:
        for n in row:
            print(" " if n == 0 else "#", end="")
        print("")


instructions = parse()
traverse(instructions)
grid = create_grid()
# print_grid()
point_within_loop = find_point_within_loop()
floodfill(point_within_loop)
# print_grid()
print(np.count_nonzero(grid == 1))
