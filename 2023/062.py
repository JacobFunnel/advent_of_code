import math
from parse import parse_lines

time, distance = [int(line.split(":")[-1].replace(" ", "")) for line in parse_lines()]
t1 = (time - (time**2 - 4 * (distance + 1)) ** 0.5) / 2
t2 = (time + (time**2 - 4 * (distance + 1)) ** 0.5) / 2
print(len(range(math.ceil(t1), math.floor(t2) + 1)))
