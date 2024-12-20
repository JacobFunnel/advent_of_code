from collections import Counter

from parse import parse_lines

grid = {}
for r, row in enumerate(parse_lines()[:-1]):
    for c, char in enumerate(row):
        grid.setdefault(char, set()).add(r + c * 1j)

[start], [end], walls, track = grid["S"], grid["E"], grid["#"], grid["."]
DIRECTIONS = [1, 1j, -1, -1j]
route = [start]
while route[-1] != end:
    current = route[-1]
    for direction in DIRECTIONS:
        new = current + direction
        if new in walls or new in route:
            continue
        route.append(new)
        break

paths_per_time_saved = Counter()
for idx, point in enumerate(route[:-100]):
    cheated_jumps = []
    for direction in DIRECTIONS:
        if point + direction in walls:
            cheated_jumps.append(point + 2 * direction)
    for cheated_point in cheated_jumps:
        if cheated_point in route and route.index(cheated_point) > idx + 2:
            time_saved = route.index(cheated_point) - (idx + 2)
            paths_per_time_saved[time_saved] += 1

print(sum(v for k, v in paths_per_time_saved.items() if k >= 100))
