import re
from itertools import combinations, pairwise
import networkx as nx

from parse import parse_lines

patterns, designs = parse_lines(2)
patterns = patterns.strip().split(", ")
designs = designs.splitlines()[:-1]

def subset_approach(patterns, designs):
    # This approach is slow as all hell
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
    return possible

def graph_path_approach(patterns, designs):
    # This approach is fast but gives wrong results, why I do not know
    possible = 0
    for design in designs:
        matching_indices = {(m.start(), m.end()) for pattern in patterns for m in re.finditer(pattern, design)}
        G = nx.Graph()
        G.add_edges_from(matching_indices)
        try:
            if nx.has_path(G, 0, len(design)):
                possible += 1
        except nx.NodeNotFound:
            continue
    return possible

def overlapping_indices_approach(patterns, designs):
    # This approach is fast and gives wrong results which is understandable
    possible = 0
    for design in designs:
        design_indices = set(range(len(design)))
        for pattern in patterns:
            matching_indices = {i for m in re.finditer(pattern, design) for i in range(m.start(), m.end())}
            design_indices -= matching_indices
            if not design_indices:
                possible += 1
                break
    return possible

print(graph_path_approach(patterns, designs))
print(overlapping_indices_approach(patterns, designs))
print(subset_approach(patterns, designs))