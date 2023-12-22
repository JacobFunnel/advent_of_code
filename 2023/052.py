from itertools import pairwise, chain
from parse import parse_lines


seeds, *categories = parse_lines(2)
seeds = chain.from_iterable(
    range(int(seed_start), int(seed_start) + int(seed_range))
    for seed_start, seed_range in list(pairwise(seeds.split()[1:]))[::2]
)

categories = [
    {
        range(source_start, source_start + range_length): source_start - destination_start
        for destination_start, source_start, range_length in [
            [int(num) for num in line.split()] for line in cat.split("\n")[1:]
        ]
    }
    for cat in categories
]
locations = []
for seed in seeds:
    item = seed
    for cat in categories:
        if item in chain.from_iterable(cat):
            destination_offset = cat[next(r for r in cat if item in r)]
            destination = item - destination_offset
            item = destination
    locations.append(item)

# Too slow
print(min(locations))
