import re
from sympy import solvers, symbols
from parse import parse_lines

coefficients = [map(int, re.findall(r"\d+", line)) for line in parse_lines(2) if line]
total = 0
for a_r, a_i, b_r, b_i, dest_r, dest_i in coefficients:
    a, b = symbols("a b", integer=True, positive=True)
    solution = solvers.solve(
        (a_r + a_i * 1j) * a + (b_r + b_i * 1j) * b - (dest_r + dest_i * 1j), a, b
    )
    if solution:
        total += solution[a] * 3 + solution[b]
print(int(total))