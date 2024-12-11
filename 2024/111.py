import math

from parse import parse_all

line = [int(n) for n in parse_all().split() if n]


def apply_rules(line):
    next_line = []
    for n in line:
        if n == 0:
            next_line.append(1)
            continue
        s = str(n)
        if len(s) % 2 == 0:
            next_line.extend([int(s[0 : len(s) // 2]), int(s[len(s) // 2 :])])
        else:
            next_line.append(n * 2024)
    return next_line

for _ in range(25):
    line = apply_rules(line)

print(len(line))
