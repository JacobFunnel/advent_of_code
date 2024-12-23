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

"""
Along the path, everytime we can enter a wall, we should consider what points we can reach by going through 
orthogonally connected walls. All points on the path that are further ahead than the point where we entered are relevant.


   .
  ...
 .....
...o...
 .....
  ...
   .
   
if we floodfill from the point where we entered the wall, then we can determine if a point on the path is reachable by
checking if is adjacent to any point in the floodfill.
"""

def reachable_from(wall_point):
    steps = 18
    columns = [range(-x, x + 1) for x in list(range(steps + 1)) + list(range(steps - 1, -1, -1))]
    rows = range(- steps, steps + 1)
    return {wall_point + (rows[i] + column * 1j) for i in range(steps * 2 + 1) for column in columns[i]}


def floodfill(point):
    global visited, path_points
    visited.add(point)
    for direction in DIRECTIONS:
        new_point = point + direction
        if new_point in visited:
            continue
        elif new_point in local_walls:
            floodfill(new_point)
        elif new_point in route:
            path_points.add(new_point)

paths_per_time_saved = Counter()
# for idx, point in enumerate(route[:-100]):
#     cheated_jumps = []
#     for direction in DIRECTIONS:
#         if point + direction in walls:
#             cheated_jumps.append(point + 2 * direction)
#     for cheated_point in cheated_jumps:
#         if cheated_point in route and route.index(cheated_point) > idx + 2:
#             time_saved = route.index(cheated_point) - (idx + 2)
#             paths_per_time_saved[time_saved] += 1


for idx, point in enumerate(route[:-100]):
    for direction in DIRECTIONS:
        if (new_point := point + direction) in walls:
            local_walls = reachable_from(new_point) & walls
            visited, path_points = set(), set()
            floodfill(new_point)
            for cheated_point in path_points:
                time_saved = route.index(cheated_point) - (idx + abs(point.real - cheated_point.real) + abs(point.imag - cheated_point.imag))
                paths_per_time_saved[time_saved] += 1

print(sum(v for k, v in paths_per_time_saved.items() if k >= 100))
print(sorted(paths_per_time_saved.items()))
