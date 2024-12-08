from itertools import combinations, permutations

from parse import parse_lines


def vector_from(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]

def add_vectors(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]

def scalar_mult(v, s):
    return v[0] * s, v[1] * s

grid = {(r, c): char for r, row in enumerate(parse_lines()[:-1]) for c, char in enumerate(row)}
antennas = {}
for point, char in grid.items():
    if char != '.':
        antennas.setdefault(char, []).append(point)

anti_nodes = set()
for antenna, points in antennas.items():
    for pair in combinations(points, 2):
        for p1, p2 in permutations(pair):
            anti_nodes.add(p1)
            vector = vector_from(p1, p2)
            n = 2
            while True:
                anti_node = add_vectors(p1, scalar_mult(vector, n))
                if anti_node in grid:
                    anti_nodes.add(anti_node)
                    n += 1
                else:
                    break

print(len(anti_nodes))
