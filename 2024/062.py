from parse import parse_lines


def turn_right(previous_direction):
    right_turns = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    return right_turns[previous_direction]

def next_position(current, direction):
    return current[0] + direction[0], current[1] + direction[1]

def walk(pos, direction):
    next_pos = next_position(pos, direction)
    if next_pos in grid:
        if grid[next_pos] == "#":
            return pos, turn_right(direction), pos, True
        else:
            return next_pos, direction, pos, True
    else:
        return pos, direction, pos, False


grid = {(r, c): char for r, row in enumerate(parse_lines()) for c, char in enumerate(row)}
start = next(k for k, v in grid.items() if v == "^")
current = start
direction = (-1, 0)
visited = {start: {direction}}
walking = True
while walking:
    current, direction, visit, walking = walk(current, direction)
    if visit:
        visited.setdefault(visit, set()).add(direction)

# mult_visits = {k: v for k, v in visited.items() if len(v) > 1}
# single_visits = {k: v for k, v in visited.items() if len(v) == 1}
obstacles = set()
# for pos, dirs in mult_visits.items():
#     for dir_ in dirs:
#         obstacle = next_position(pos, dir_)
#         if turn_right(dir_) in dirs:
#             obstacles.add(obstacle)
#
# print(len(obstacles))

for pos, dirs in visited.items():
    for dir_ in dirs:
        obstacle = next_position(pos, dir_)
        if obstacle not in grid or grid[obstacle] == "#":
            continue
        else:
            whatever_was_there = grid[obstacle]
            grid[obstacle] = "#"
        direction = turn_right(dir_)
        current = pos
        walking = True
        new_visits = {}
        while walking:
            current, direction, visit, walking = walk(current, direction)
            if direction in new_visits.get(visit, set()):
                obstacles.add(obstacle)
                grid[obstacle] = whatever_was_there
                break
            elif dir:
                new_visits.setdefault(visit, set()).add(direction)
        grid[obstacle] = whatever_was_there
print(len(obstacles))
