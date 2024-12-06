import re
from itertools import batched
from functools import cmp_to_key

from parse import parse_lines


raw_rules, raw_to_print_lines = parse_lines(2)
rules = {}
for a, b in batched(re.split(r"[|\n]", raw_rules), 2):
    rules.setdefault(int(a), set()).add(int(b))
to_print_lines = [[int(n) for n in line.split(",")] for line in raw_to_print_lines.splitlines() if line]

def sort_cmp(a, b):
    return -1 if b in rules.get(a, set()) else 0

total = 0
for line in to_print_lines:
    sorted_line = sorted(line, key= cmp_to_key(sort_cmp))
    if sorted_line != line:
        total += sorted_line[len(sorted_line)//2]

print(total)
