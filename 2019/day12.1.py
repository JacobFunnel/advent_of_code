from itertools import combinations
import re

with open("input/12.txt", "r") as f:
    # r'-?\d+' dash (minus) is optional, then match one or more digits
    positions = [tuple(int(n) for n in re.findall(r'-?\d+', line)) for line in f.readlines()]
    velocities = [tuple(0 for a in range(3)) for b in range(4)]


def compare(a, b):
    return -1 if a > b else 0 if a == b else 1


def gravity_shift(p1, p2):
    p1_shift = tuple(compare(p1[i], p2[i]) for i in range(len(p1)))
    p2_shift = tuple(-x for x in p1_shift)
    return p1_shift, p2_shift


def sum_vectors(vectors):
    return tuple(sum(n) for n in zip(*vectors))


def update_p_v(positions, velocities):
    shifts = {position: [] for position in positions}
    for p1, p2 in combinations(positions, 2):
        p1_shift, p2_shift = gravity_shift(p1, p2)
        shifts[p1].append(p1_shift)
        shifts[p2].append(p2_shift)

    gravity_velocities = [sum_vectors(v) for v in shifts.values()]
    new_velocities = [sum_vectors((velocities[i], gravity_velocities[i])) for i in range(4)]
    new_positions = [sum_vectors((positions[i], new_velocities[i])) for i in range(4)]
    return new_positions, new_velocities


for i in range(1000):
    positions, velocities = update_p_v(positions, velocities)

print(
    sum(
        [sum([abs(a) for a in p]) * sum([abs(b) for b in v]) for p, v in zip(positions, velocities)]
    )
)
