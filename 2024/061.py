from parse import parse_lines

grid = {(r, c): char for r, row in enumerate(parse_lines()) for c, char in enumerate(row)}
start = next(k for k, v in grid.items() if v == "^")
visited = {start}


def turn(previous_direction):
    right_turns = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    return right_turns[previous_direction]


def walk(current, direction):
    global visited
    next_pos = (current[0] + direction[0], current[1] + direction[1])
    if next_pos in grid:
        if grid[next_pos] == "#":
            walk(current, turn(direction))
        else:
            visited.add(current)
            walk(next_pos, direction)
    else:
        visited.add(current)
        exit()


walk(start, (-1, 0))