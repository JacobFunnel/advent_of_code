from itertools import pairwise
from parse import parse_lines


ranges, _ = parse_lines(2)
ranges = sorted(tuple(map(int, r.split("-"))) for r in ranges.splitlines())


def merge_ranges():
    global ranges
    for (i1, r1), (i2, r2) in pairwise(enumerate(ranges)):
        a1, b1 = r1
        a2, b2 = r2
        if a1 <= a2 <= b1 or a2 == b1 + 1:
            if b2 < b1:
                ranges[i1 : i2 + 1] = [(a1, b1)]
                return False
            else:
                ranges[i1 : i2 + 1] = [(a1, b2)]
                return False
    return True


while not merge_ranges():
    pass

print(sum(b - a + 1 for a, b in ranges))
