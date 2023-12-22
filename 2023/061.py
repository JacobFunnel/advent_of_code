import math
from parse import parse_lines

times, distances = [[int(n) for n in line.split(":")[-1].split()] for line in parse_lines()]
ways_to_win = []

for time, distance in zip(times, distances):
    t1 = (time - (time**2 - 4 * (distance + 1)) ** 0.5) / 2
    t2 = (time + (time**2 - 4 * (distance + 1)) ** 0.5) / 2
    ways_to_win.append(len(range(math.ceil(t1), math.floor(t2) + 1)))

print(math.prod(ways_to_win))
