from itertools import combinations, pairwise

from parse import parse_lines

reports = [[int(n) for n in line.split()] for line in parse_lines() if line]
are_safe = 0
for report in reports:
    is_safe = False
    for combo in combinations(report, len(report) - 1):
        differences = [a - b for a, b in pairwise(combo)]
        if (
            all(map(lambda x: x < 0, differences))
            and min(differences) >= -3
            and max(differences) <= -1
        ) or (
            all(map(lambda x: x > 0, differences))
            and min(differences) >= 1
            and max(differences) <= 3
        ):
            is_safe = True
            break
    if is_safe:
        are_safe += 1

print(are_safe)
