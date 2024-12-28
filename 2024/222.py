from collections import Counter
from itertools import pairwise, islice, tee

from parse import parse_lines


class SetOnceDict(dict):
    def __setitem__(self, key, value):
        if not key in self:
            super(SetOnceDict, self).__setitem__(key, value)


def n_wise(iterable, n):
    n_iterators = tee(iterable, n)
    zippables = (islice(it, j, None) for j, it in enumerate(n_iterators))
    return zip(*zippables)


def next_number(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ (n // 32)) % 16777216
    return (n ^ (n * 2048)) % 16777216

numbers = [int(line) for line in parse_lines() if line]
prices_per_round = []
for _ in range(2000):
    numbers = [next_number(number) for number in numbers]
    prices_per_round.append([int(str(number)[-1]) for number in numbers])

prices_per_monkey = list(map(list, zip(*prices_per_round)))
diffs_per_monkey = [
    [after - before for before, after in pairwise(prices)] for prices in prices_per_monkey
]
seqs = [
    SetOnceDict((seq, prices_per_monkey[monkey][idx + 4]) for idx, seq in enumerate(n_wise(diffs, 4)))
    for monkey, diffs in enumerate(diffs_per_monkey)
]
totals = Counter()
for seq in seqs:
    for k, price in seq.items():
        totals[k] += price

print(totals[max(totals, key=totals.get)])
# Doesn't work for the input, but works for the example, no idea why
