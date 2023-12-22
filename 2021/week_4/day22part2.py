import time

start_time = time.time()

with open("../input/day22_input.txt", "r") as f:
    filelines = [line.split() for line in f.readlines()]

instructions = []

for line in filelines:
    switch, rest = line
    rest = rest.split(",")
    rest = [[xyz[0], *xyz[2:].split("..")] for xyz in rest]
    d = {}
    for xyz in rest:
        d.update({xyz[0]: (int(xyz[1]), int(xyz[2]))})
    instructions.append((switch, d))


def overlapping(a, b):
    overlap = {}
    for i in ["x", "y", "z"]:
        if a[i][1] >= b[i][0] and a[i][0] <= b[i][1]:
            overlap.update({i: (max(a[i][0], b[i][0]), min(a[i][1], b[i][1]))})
        else:
            return False
    return overlap


def volume(coordinates):
    (x1, x2), (y1, y2), (z1, z2) = coordinates.values()
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1) * (abs(z2 - z1) + 1)


print(instructions[0][1])
print(instructions[1][1])
print("intersection: ", overlapping(instructions[0][1], instructions[1][1]), "\n")
print(instructions[2][1], "\n")
print("intersection 0: ", overlapping(instructions[2][1], instructions[0][1]))
print("intersection 1: ", overlapping(instructions[2][1], instructions[1][1]))
print(
    "intersection with intersection: ",
    overlapping(instructions[2][1], overlapping(instructions[0][1], instructions[1][1])),
)
