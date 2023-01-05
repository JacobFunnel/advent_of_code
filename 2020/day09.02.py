from itertools import combinations

with open("input/09.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    return [int(line) for line in lines]


def find_error(numbers):
    for i, number in enumerate(numbers):
        if i >= 25:
            pairs = combinations(numbers[i-25:i], 2)
            pair_sums = {sum(pair) for pair in pairs}
            if number not in pair_sums:
                return i


def find_set(numbers, index):
    goal = numbers[index]
    search_space = numbers[:index]
    for i, number in enumerate(search_space):
        i_sum = [number]
        x = 0
        while sum(i_sum) < goal:
            x += 1
            i_sum.append(search_space[i+x])
            if sum(i_sum) == goal:
                return i_sum


numbers = parse(lines)
index = find_error(numbers)
series = find_set(numbers, index)
print(min(series) + max(series))
