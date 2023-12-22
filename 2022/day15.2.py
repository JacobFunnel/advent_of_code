import re

with open("input/15.txt", "r") as f:
    coords = [tuple(map(int, re.findall(r"-?\d+", row))) for row in f.read().splitlines()]
    s_b = {(x1, y1): (x2, y2) for x1, y1, x2, y2 in coords}


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def overlap(s1, e1, s2, e2):
    return e1 >= s2 and e2 >= s1


def simplify_range(x_range):
    try:
        a, b = x_range[1:3]
        if b == a + 1:
            x_range = simplify_range(x_range[0:1] + x_range[3:])
    except ValueError:
        pass
    return x_range


xymin = 0
xymax = 4000000
excl_ranges_by_y = {}
for sensor, beacon in s_b.items():
    max_dist = manhattan(sensor, beacon)
    x, y = sensor
    dy = 0
    for n in range(max_dist, -1, -1):
        if overlap(x - n, x + n, xymin, xymax):
            excl_ranges_by_y.setdefault(y + dy, []).append((max(x - n, xymin), min(x + n, xymax)))
            excl_ranges_by_y.setdefault(y - dy, []).append((max(x - n, xymin), min(x + n, xymax)))
        dy -= 1

excl_ranges_by_y = {k: v for k, v in excl_ranges_by_y.items() if xymin <= k <= xymax}
for y, x_ranges in excl_ranges_by_y.items():
    points = []
    for start, end in sorted(x_ranges):
        points.extend([(start, 0), (end, 1)])
    count, previous = 0, 0
    new_ranges = []
    for point, end in sorted(points):
        count += -1 if end else 1
        if (previous, count) in [(0, 1), (1, 0)]:
            new_ranges.append(point)
        previous = count
    simplified_range = simplify_range(new_ranges)
    if simplified_range != [xymin, xymax]:
        if len(simplified_range) == 4:
            x = simplified_range[1] + 1
        else:
            x = xymin if simplified_range[0] != xymin else xymax
        print(f"Beacon at ({x}, {y}) " f"with tuning frequency: {x * 4000000 + y}")
        break
