import re
from itertools import product

from parse import parse_lines

equations = [list(map(int, re.split(r": | ", line))) for line in parse_lines()[:-1]]
OPERATORS = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "||": lambda x, y: int(str(x) + str(y)),
}

def solve(equation):
    total = equation[0]
    permutations = product(OPERATORS.values(), repeat=len(equation[1:]) - 1)
    for permutation in permutations:
        numbers = equation[1:]
        temp_total = numbers.pop(0)
        for operator in permutation:
            temp_total = operator(temp_total, numbers.pop(0))
        if temp_total == total:
            return total
    return 0

print(sum(solve(equation) for equation in equations))
