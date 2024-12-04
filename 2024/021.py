from itertools import pairwise

from parse import parse_lines

reports = [[int(n) for n in line.split()] for line in parse_lines() if line]
safe = 0
for report in reports:
    differences = [a - b for a, b in pairwise(report)]
    if all(map(lambda x: x < 0, differences)) and min(differences) >= -3 and max(differences) <= -1:
        safe += 1
    if all(map(lambda x: x > 0, differences)) and min(differences) >= 1 and max(differences) <= 3:
        safe += 1

print(safe)
