with open("input/03.txt", "r") as f:
    instructions = [[(s[0], int(s[1:])) for s in line.split(",")] for line in f.read().split("\n")]


def mul(v, s):
    return s * v[0], s * v[1]


def add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


def line_points(pos, v, s):
    points = set()
    for value in range(s + 1):
        points.add(add(pos, mul(v, value)))
    return points


def manhattan(point):
    return abs(point[0]) + abs(point[1])


directions = {"R": (1, 0), "D": (0, -1), "L": (-1, 0), "U": (0, 1)}
points = {0: set(), 1: set()}
for idx, line in enumerate(instructions):
    current_pos = (0, 0)
    for d, amount in line:
        points[idx] |= line_points(current_pos, directions[d], amount)
        current_pos = add(current_pos, mul(directions[d], amount))

manhattans = []
for point in set.intersection(*points.values()) ^ {(0, 0)}:
    manhattans.append(manhattan(point))

print(min(manhattans))
