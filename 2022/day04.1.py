import re

with open("input/04.txt", "r") as f:
    range_quads = [tuple(map(int, re.findall(r"\d+", line))) for line in f.read().splitlines()]


def issubrange(range_quad):
    a1, a2, b1, b2 = range_quad
    return (a1 >= b1 and a2 <= b2) or (a1 <= b1 and a2 >= b2)


print(sum(1 for quad in range_quads if issubrange(quad)))
