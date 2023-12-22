from parse import parse_lines

seeds, *categories = parse_lines(2)
seeds = [int(seed) for seed in seeds.split()[1:]]
categories = [
    sorted(
        ([int(num) for num in line.split()] for line in cat.split("\n")[1:]),
        key=lambda nums: nums[1],
    )
    for cat in categories
]
locations = []
for seed in seeds:
    item = seed
    for cat in categories:
        for destination_start, source_start, range_length in cat:
            if item in range(source_start, source_start + range_length):
                destination = item - source_start + destination_start
                item = destination
                break
            elif item < source_start:
                break
    locations.append(item)

print(min(locations))
