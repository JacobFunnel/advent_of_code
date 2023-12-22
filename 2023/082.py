from parse import parse_lines
from itertools import cycle

directions, network = parse_lines(2)
directions = [0 if d == "L" else 1 for d in directions]
network = {line[:3]: (line[7:10], line[12:15]) for line in network.splitlines()}

start_locs = [key for key in network.keys() if key.endswith("A")]
steps_to_reach_z = {location: [] for location in start_locs}
step = 0
prev_locs = start_locs
for direction in cycle(directions):
    step += 1
    next_locs = [network[prev_loc][direction] for prev_loc in prev_locs]
    if set(start_locs).intersection(set(next_locs)):
        print(start_locs, next_locs)
    for start_loc, next_loc in zip(start_locs, next_locs):
        if start_loc == next_loc:
            steps_to_reach_z[start_loc].append(step)
    prev_locs = next_locs
    if all(steps_to_reach_z.values()):
        break

print(steps_to_reach_z)
