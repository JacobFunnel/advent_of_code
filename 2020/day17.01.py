with open("input/17.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    active = set()
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == "#":
                active.add((x, y, 0))
    return active


def find_neighbors(coord=(0, 0, 0)):
    x, y, z = coord
    directions = {(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1)}
    neighbors = {(x + a, y + b, z + c) for (a, b, c) in directions} - {coord}
    return neighbors


def conway(active, n):
    for i in range(n):
        neighbors = {}
        for coord in active:
            neighbors[coord] = find_neighbors(coord)
        pos_to_check = {element for neighbor in neighbors.values() for element in neighbor}
        inactive = pos_to_check - active
        to_activate = set()
        for element in inactive:
            if len(find_neighbors(element).intersection(active)) == 3:
                to_activate.add(element)
        for element in active:
            if len(find_neighbors(element).intersection(active - {element})) in (2, 3):
                to_activate.add(element)
        active = to_activate

    return len(active)


initially_active = parse(lines)
print(conway(initially_active, 6))
