with open("input/03.txt", "r") as f:
    instructions = [[(s[0], int(s[1:])) for s in line.split(",")] for line in f.read().split("\n")]


def mul(v, s):
    return s * v[0], s * v[1], s * v[2]


def add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]


def line_points(pos, v, s):
    points = set()
    for value in range(s + 1):
        points.add(add(pos, mul(v, value)))
    return points


def manhattan(point):
    return abs(point[0]) + abs(point[1])


directions = {"R": (1, 0, 1), "D": (0, -1, 1), "L": (-1, 0, 1), "U": (0, 1, 1)}
points_3d = {0: set(), 1: set()}
for idx, line in enumerate(instructions):
    current_pos = (0, 0, 0)  # (x, y, steps_taken)
    for d, amount in line:
        points_3d[idx] |= line_points(current_pos, directions[d], amount)
        current_pos = add(current_pos, mul(directions[d], amount))


points_2d = {idx: {(p[0], p[1]) for p in ps} for idx, ps in points_3d.items()}
intersections_2d = set.intersection(*points_2d.values()) ^ {(0, 0)}
intersections_3d = {}
for idx, points in points_3d.items():
    for p in points:
        p_2d = p[0], p[1]
        if p_2d in intersections_2d:
            intersections_3d[p_2d] = intersections_3d.setdefault(p_2d, 0) + p[2]

print(min(intersections_3d.values()))
