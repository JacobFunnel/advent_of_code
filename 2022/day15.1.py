import re

with open("input/15.txt", "r") as f:
    coords = [tuple(map(int, re.findall(r"-?\d+", row))) for row in f.read().splitlines()]
    s_b = {(x1, y1): (x2, y2) for x1, y1, x2, y2 in coords}


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def in_range(item, a, b):
    if a <= item <= b:
        return min(abs(item - a), abs(b - item))
    else:
        return None


target = 2000000
exclusion_ranges = []
for sensor, beacon in s_b.items():
    max_dist = manhattan(sensor, beacon)
    x, y = sensor
    dx = in_range(target, y - max_dist, y + max_dist)
    if dx is not None:
        exclusion_ranges.append((x - dx, x + dx))

sb_on_target_line = [x for x, y in set(s_b.keys()) | set(s_b.values()) if y == target]
points = []
for start, end in sorted(exclusion_ranges):
    points.extend([(start, 0), (end, 1)])
count, previous = 0, 0
new_ranges = []
for point, end in sorted(points):
    count += -1 if end else 1
    if (previous, count) in [(0, 1), (1, 0)]:
        new_ranges.append(point)
    previous = count

total = 0
for a, b in zip(new_ranges[0::2], new_ranges[1::2]):
    for sb in sb_on_target_line:
        if in_range(sb, a, b):
            total -= 1
    total += b - a + 1
print(total)
