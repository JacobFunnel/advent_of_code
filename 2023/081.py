from parse import parse_lines
from itertools import cycle

directions, network = parse_lines(2)
directions = [0 if d == "L" else 1 for d in directions]
network = {line[:3]: (line[7:10], line[12:15]) for line in network.splitlines()}

location = "AAA"
step = 0
for direction in cycle(directions):
    step += 1
    location = network[location][direction]
    if location == "ZZZ":
        break

print(step)
