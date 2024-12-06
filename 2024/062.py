"""
If we keep track of the vectors that the guard moves through each position, we can for each step check if an obstacle
would make the guard repeat a previous vector for that position. If he does, then he will be stuck in a loop
"""

from parse import parse_lines


def turn(previous_direction):
    right_turns = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    return right_turns[previous_direction]

def next_position(current, direction):
    return (current[0] + direction[0], current[1] + direction[1])

def walk(current, direction):
    global visited
    next_pos = next_position(current, direction)
    if next_pos in grid:
        if grid[next_pos] == "#":
            return current, turn(direction), True
        else:
            visited.setdefault(current, set()).add(direction)
            return next_pos, direction, True
    else:
        visited.setdefault(current, set()).add(direction)
        return current, direction, False


grid = {(r, c): char for r, row in enumerate(parse_lines()) for c, char in enumerate(row)}
start = next(k for k, v in grid.items() if v == "^")
current = start
direction = (-1, 0)
visited = {start: {direction}}
walking = True
while walking:
    current, direction, walking = walk(current, direction)
mult_visits = {k: v for k, v in visited.items() if len(v) > 1}
for pos, dirs in mult_visits.items():
    for dir_ in dirs:
        """
        If we can place an obstacle in the path of the guard and check if that results in the guard
        revisiting a previous vector then we know it will cause a loop
        """
        turn(dir_)
        while next_position(pos, dir_) in grid:
            pass

