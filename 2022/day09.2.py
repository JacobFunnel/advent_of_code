with open("input/09.txt", "r") as f:
    destinations = [(line.split()[0], int(line.split()[1])) for line in f.read().splitlines()]

knots = [(0, 0) for _ in range(10)]
d_coord = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
visited = {(0, 0)}


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sign(a):
    return int(abs(a) / a) if a else 0


def get_direction(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if abs(dx) > 1 or abs(dy) > 1:
        return sign(dx), sign(dy)
    else:
        return 0, 0


for d, amount in destinations:
    for _ in range(amount):
        knots[0] = add(knots[0], d_coord[d])
        for i in range(1, len(knots)):
            knots[i] = add(knots[i], get_direction(knots[i - 1], knots[i]))
        visited.add(knots[-1])

print(len(visited))
