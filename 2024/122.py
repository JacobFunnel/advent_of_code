from collections import Counter

from parse import parse_lines

chars = {}
for r, row in enumerate(parse_lines()[:-1]):
    for c, char in enumerate(row):
        chars.setdefault(char, set()).add(r + c * 1j)

DIRECTIONS = [1, 1j, -1, -1j]
edges = {}
farms = []
counter = Counter()


def fence_between(p1, p2):
    midpoint = (p1.real + p2.real) / 2 + (p1.imag + p2.imag) / 2 * 1j
    vector_between = p2 - p1
    if vector_between.real == 0:
        return midpoint + 0.5, midpoint - 0.5
    else:
        return midpoint + 0.5j, midpoint - 0.5j


def fence_sides(fences):
    vertical, horizontal = {}, {}
    for p1, p2 in fences:
        if (p2 - p1).imag:
            horizontal.setdefault(p1.imag, []).extend([p1.real, p2.real])
        else:
            vertical.setdefault(p1.real, []).extend([p1.imag, p2.imag])
    all_sides = 0
    for vertices in list(vertical.values()) + list(horizontal.values()):
        sides = 1
        for idx, n in enumerate(sorted(set(vertices))):
            if idx > 0:
                if not n == vertices[idx - 1]:
                    sides += 1
        all_sides += sides
    return all_sides


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
            edges.setdefault(point, []).append(new_point)


for char, points in chars.items():
    while points:
        point = points.pop()
        visited = set()
        floodfill(point)
        farms.append(visited)
        points -= visited

fences = {
    point: [fence_between(point, neighbor) for neighbor in neighbors]
    for point, neighbors in edges.items()
}

for farm in farms:
    farm_fences = [fence for point in farm for fence in fences.get(point, [])]
    print(fence_sides(farm_fences))
