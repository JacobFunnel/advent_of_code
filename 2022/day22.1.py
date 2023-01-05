import re
import numpy

with open("input/22.txt", "r") as f:
    raw_grid, raw_movements = f.read().split("\n\n")
    lines = [line for line in raw_grid.splitlines()]
    width = len(max(lines, key=len))
    grid = numpy.array([[char for char in line.ljust(width)[:width]] for line in lines])
    movements = [int(move) if i % 2 == 0 else move
                 for i, move in enumerate(re.findall(r'\D|\d+', raw_movements))]

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # >, ^, <, v
direction = directions[0]
d_score = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
position = (0, lines[0].find("."))
height, width = grid.shape


def get_direction(move):
    global directions
    if move == "R":
        directions.insert(0, directions.pop())
    elif move == "L":
        directions.append(directions.pop(0))
    return directions[0]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def wrap_around(position, direction):
    y, x = position
    dy, dx = direction
    if dy:
        column = "".join(grid[:, x])
        tiles = re.search(r'\S', column)
        if dy > 0:
            y = tiles.start()
        else:
            y = tiles.end()
    elif dx:
        row = "".join(grid[:, x])
        tiles = re.search(r'\S', row)
        if dx > 0:
            x = tiles.start()
        else:
            x = tiles.end()
    return y, x


def in_range(new_position):
    y, x = new_position
    return y in range(height) and x in range(width)


for idx, move in enumerate(movements):
    if idx % 2 != 0:
        direction = get_direction(move)
    else:
        for step in range(move):
            new_position = add(position, direction)
            if not in_range(new_position):
                new_position = wrap_around(position, direction)
            tile = grid[new_position]
            if tile == " ":
                new_position = wrap_around(position, direction)
                tile = grid[new_position]
            if tile == "#":
                break
            position = new_position

y, x = position
column = x + 1
row = y + 1
facing = d_score[direction]
print(f"row: {row}\n"
      f"column: {column}\n"
      f"facing: {facing}\n"
      f"password: {1000 * row + 4 * column + facing}")
