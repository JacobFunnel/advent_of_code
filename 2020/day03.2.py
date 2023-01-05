from collections import deque
from copy import deepcopy

with open("input/03.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    treemap = []
    for line in lines:
        treemap.append(deque([1 if char == "#" else 0 for char in line]))
    return treemap


def count_trees(treemap, x_slope, y_slope):
    trees, x, y = 0, 0, 0
    while True:
        x += x_slope
        y += y_slope
        try:
            line = treemap[y]
            line.rotate_90(-x)
            if line[0] == 1:
                trees += 1
        except IndexError:
            return trees


treemap = parse(lines)
prod = 1
for x_slope, y_slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    prod *= count_trees(deepcopy(treemap), x_slope, y_slope)
print(prod)
