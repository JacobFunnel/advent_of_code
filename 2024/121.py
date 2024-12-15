from collections import Counter

from parse import parse_lines




def floodfill(point):
    global visited
    global points
    global edges
    visited.add(point)
    for direction in DIRECTIONS:
        new_point = point + direction
        if new_point in visited:
            continue
        elif new_point in points:
            floodfill(new_point)
        else:
            edges[point] += 1


DIRECTIONS = [1, 1j, -1, -1j]
edges = Counter()
farms = []
crop_points = {}
for r, row in enumerate(parse_lines()[:-1]):
    for c, char in enumerate(row):
        crop_points.setdefault(char, set()).add(r + c * 1j)

for char, points in crop_points.items():
    while points:
        point = points.pop()
        visited = set()
        floodfill(point)
        farms.append(visited)
        points -= visited

print(sum(len(farm) * sum(edges[point] for point in farm) for farm in farms))