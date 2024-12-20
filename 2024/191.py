from itertools import combinations, pairwise

from parse import parse_lines

patterns, designs = parse_lines(2)
patterns = set(patterns.strip().split(", "))
designs = designs.splitlines()[:-1]
possible = 0
for design in designs:
    start, end = 0, len(design)
    indices = range(1, end)
    split_indices_collection = (combo for idx in indices for combo in combinations(indices, idx))
    sub_pattern_collection = (
        {design[idx1:idx2] for idx1, idx2 in pairwise((start,) + split_indices + (end,))}
        for split_indices in split_indices_collection
    )
    if any(sub_patterns.issubset(patterns) for sub_patterns in sub_pattern_collection):
        possible += 1

print(possible)
