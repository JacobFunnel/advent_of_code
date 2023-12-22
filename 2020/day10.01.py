with open("input/10.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    return sorted([int(line) for line in lines])


def calc_diffs(joltages):
    diffs = {1: 0, 2: 0, 3: 1}
    for i, joltage in enumerate(joltages):
        if i == 0:
            diffs[joltage] += 1
        else:
            diffs[joltage - joltages[i - 1]] += 1
    return diffs


joltages = parse(lines)
diffs = calc_diffs(joltages)
print(diffs[1] * diffs[3])
