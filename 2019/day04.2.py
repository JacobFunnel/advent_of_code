from itertools import groupby

with open("input/04.txt", "r") as f:
    limits = [int(n) for n in f.read().split("-")]


def check(n):
    return n[0] <= n[1] <= n[2] <= n[3] <= n[4] <= n[5] and any(
        [True for _, g in groupby(n) if len(list(g)) == 2]
    )


valid = 0
for n in range(limits[0], limits[1] + 1):
    if check(str(n)):
        valid += 1

print(valid)
