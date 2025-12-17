from itertools import batched
from parse import parse_all

pairs = (tuple(map(int, block.split("-"))) for block in parse_all().split(","))
total = 0
for s, e in pairs:
    for n in range(s, e + 1):
        s = str(n)
        l = len(s)
        sizes = [divisor for divisor in range(l - 1, 0, -1) if l % divisor == 0]
        for size in sizes:
            batches = batched(s, size)
            if len({batch for batch in batches}) == 1:
                total += n
                break

print(total)
