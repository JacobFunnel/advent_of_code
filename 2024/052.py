import re
from itertools import batched

from parse import parse_lines


raw_rules, raw_to_print_lines = parse_lines(2)
rules = {}
for a, b in batched(re.split(r"[|\n]", raw_rules), 2):
    rules.setdefault(int(a), set()).add(int(b))
to_print_lines = [[int(n) for n in line.split(",")] for line in raw_to_print_lines.splitlines() if line]

print(set(rules.keys()).union({v for s in rules.values() for v in s}))
total = 0
for line in to_print_lines:
    valid = True
    for idx, page in enumerate(line):
        if set(line[:idx]).intersection(rules.get(page, set())):
            valid = False
            break
    if valid:
        total += line[len(line)//2]

print(total)