with open("input/18.txt", "r") as f:
    cubes = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]


def sides(cube):
    x, y, z = cube
    offsets = [
        (0.5, 0, 0),
        (-0.5, 0, 0),
        (0, 0.5, 0),
        (0, -0.5, 0),
        (0, 0, 0.5),
        (0, 0, -0.5),
    ]
    return [(x + dx, y + dy, z + dz) for dx, dy, dz in offsets]


all_sides = []
for cube in cubes:
    all_sides.extend(sides(cube))

print(len(all_sides) - 2 * (len(all_sides) - len(set(all_sides))))
