import re
from math import prod
from collections import namedtuple
from parse import parse_lines

Entity = namedtuple("Number", ["value", "row", "start_column", "end_column", "coords"])
rows = parse_lines()
row_idx_max = len(rows) - 1
col_idx_max = len(rows[0]) - 1
numbers = [
    Entity(
        int(m.group()),
        idx,
        m.start(),
        m.end() - 1,
        tuple((idx, col) for col in range(m.start(), m.end())),
    )
    for idx, row in enumerate(rows)
    for m in re.finditer(r"\d+", row)
]
asterisks = [
    Entity(
        0,
        idx,
        m.start(),
        m.end() - 1,
        ((idx, col) for col in range(m.start(), m.end())),
    )
    for idx, row in enumerate(rows)
    for m in re.finditer(r"\*", row)
]
number_coords = {(r, c): n for n in numbers for r, c in n.coords}


def neighborhood(n: Entity):
    to_check = {(n.row, n.start_column - 1), (n.row, n.end_column + 1)}
    for col in range(n.start_column - 1, n.end_column + 2):
        to_check.add((n.row - 1, col))
        to_check.add((n.row + 1, col))
    return {(r, c) for r, c in to_check if 0 <= r <= row_idx_max and 0 <= c <= col_idx_max}


total = 0
for asterisk in asterisks:
    matched_numbers = {
        number_coords[coord] for coord in neighborhood(asterisk) if coord in number_coords
    }
    if len(matched_numbers) == 2:
        total += prod((n.value for n in matched_numbers))

print(total)
