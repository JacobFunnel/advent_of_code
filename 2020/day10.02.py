with open("input/10.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    return sorted([int(line) for line in lines])


# 1 2 5 6 7 8


def consecutive_joltages(joltages):
    splits_by_indices = {}
    streak_idx = 0
    streak = 0
    for i, jolt in enumerate(joltages):
        diff = joltages[min(i + 1, len(joltages) - 1)] - jolt
        if diff == 3:
            if streak > 0:
                splits_by_indices[streak_idx] += 1
                streak += 1
            else:
                splits_by_indices[i] = 1
                streak_idx = i
                streak = 1
        elif diff == 1:
            streak = 0
        elif diff == 0:
            return splits_by_indices


def split_joltages(joltages, splits_by_indices):
    new = []
    for i, count in splits_by_indices.items():
        new.append(joltages[i : i + count + 1])


def combinations(joltages):
    if len(joltages) == 1:
        return 1
    elif len(joltages) == 2:
        return 2
    else:
        pass


def calc_combinations(joltages):
    pass


joltages = parse(lines)
print(split_joltages(joltages, consecutive_joltages(joltages)))
