import re
from collections import namedtuple
from parse import parse_lines

number = namedtuple("Number", ["value", "row", "start_column", "end_column"])
rows = parse_lines()
row_idx_max = len(rows) - 1
col_idx_max = len(rows[0]) - 1
numbers = [
    number(int(m.group()), idx, m.start(), m.end() - 1)
    for idx, row in enumerate(rows)
    for m in re.finditer(r"\d+", row)
]


def neighborhood(n: number):
    to_check = {(n.row, n.start_column - 1), (n.row, n.end_column + 1)}
    for col in range(n.start_column - 1, n.end_column + 2):
        to_check.add((n.row - 1, col))
        to_check.add((n.row + 1, col))
    return {(r, c) for r, c in to_check if 0 <= r <= row_idx_max and 0 <= c <= col_idx_max}


total = 0
for n in numbers:
    adjacent = False
    for r, c in neighborhood(n):
        if rows[r][c] not in ".123456789":
            adjacent = True
            break
    if adjacent:
        total += n.value

print(total)
