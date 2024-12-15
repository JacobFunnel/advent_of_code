from itertools import pairwise

from parse import parse_lines

DIRECTIONS = [1, 1j, -1, -1j]
chars, edges, farms = {}, {}, {}
for r, row in enumerate(parse_lines()[:-1]):
    for c, char in enumerate(row):
        chars.setdefault(char, set()).add(r + c * 1j)


def fence_between(p1, p2):
    midpoint = (p1.real + p2.real) / 2 + (p1.imag + p2.imag) / 2 * 1j
    vector_between = p2 - p1
    if vector_between.real == 0:
        return midpoint + 0.5, midpoint - 0.5
    else:
        return midpoint + 0.5j, midpoint - 0.5j


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


def revisited_node(end, chain):
    try:
        return [start for start, *_ in chain].index(end)
    except ValueError:
        return False


def create_loops(fences):
    loop, loops = [], []
    while fences:
        fence = fences.pop()
        while True:
            start, end = fence
            if len(loop) > 0 and start != loop[-1][1]:
                start, end = end, start
            direction = end - start
            directed_fence = (start, end, direction)
            loop.append(directed_fence)
            if (revisited_node_idx := revisited_node(end, loop)) is not False:
                loops.append(rotate(loop[revisited_node_idx:]))
                loop = loop[:revisited_node_idx]
                if not loop:
                    break
            try:
                next_idx = [idx for idx, f in enumerate(fences) if end in f].pop()
                fence = fences.pop(next_idx)
            except IndexError:
                loops.append(rotate(loop))
                loop = []
                break
    return loops


def rotate(loop):
    while True:
        (*_, first_direction), (*_, last_direction) = loop[0], loop[-1]
        if first_direction == last_direction:
            loop.insert(0, loop.pop())
        else:
            return loop


def count_sides(loop):
    sides = 1
    for (*_, previous_direction), (*_, direction) in pairwise(loop):
        if previous_direction != direction:
            sides += 1
    return sides


for char, points in chars.items():
    while points:
        point = points.pop()
        visited = set()
        floodfill(point)
        farms.setdefault(char, []).append(visited)
        points -= visited

fences = {
    point: [fence_between(point, neighbor) for neighbor in neighbors]
    for point, neighbors in edges.items()
}

total = 0
for char, plots in farms.items():
    for plot in plots:
        plot_fences = [fence for point in plot for fence in fences.get(point, [])]
        total += len(plot) * sum(count_sides(chain) for chain in create_loops(plot_fences))
print(total)
