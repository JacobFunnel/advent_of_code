from collections import deque

with open("input/03.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    treemap = []
    for line in lines:
        treemap.append(deque([1 if char == "#" else 0 for char in line]))
    return treemap


def count_trees(treemap):
    trees, x, y = 0, 0, 0
    while True:
        x += 3
        y += 1
        try:
            line = treemap[y]
            line.rotate_90(-x)
            if line[0] == 1:
                trees += 1
        except IndexError:
            return trees


print(count_trees(parse(lines)))
