import math
from parse import parse_all

line = [int(n) for n in parse_all().split() if n]

def apply_rules(n):
    if n == 0:
        return (1,)
    digits = int(math.log10(n)) + 1
    if digits % 2 == 0:
        factor = 10 ** (digits // 2)
        return (n - n % factor) // factor, n % factor
    else:
        return (n * 2024,)

for blink in range(75):
    # doesn't work for 75 iterations
    line = [new_n for n in line for new_n in apply_rules(n)]

print(len(line))
