import re

with open("input/04.txt", "r") as f:
    range_quads = [tuple(map(int, re.findall(r"\d+", line))) for line in f.read().splitlines()]


def overlap(range_quad):
    a1, a2, b1, b2 = range_quad
    return set(range(a1, a2 + 1)).intersection(set(range(b1, b2 + 1)))


print(sum(1 for quad in range_quads if overlap(quad)))
