from itertools import combinations

with open("input/09.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    return [int(line) for line in lines]


def find_error(numbers):
    for i, number in enumerate(numbers):
        if i >= 25:
            pairs = combinations(numbers[i - 25 : i], 2)
            pair_sums = {sum(pair) for pair in pairs}
            if number not in pair_sums:
                return number


numbers = parse(lines)
print(find_error(numbers))
