from sympy import solve

with open("input/21.txt", "r") as f:
    monkeys = {line[:4]: line[6:].split() for line in f.read().splitlines()}
    monkeys["root"][1] = "="
    monkeys["humn"] = ["n"]


def find_expression(monkey):
    if len(monkeys[monkey]) == 1:
        n = monkeys[monkey][0]
        return n
    else:
        m1, op, m2 = monkeys[monkey]
        return f"({find_expression(m1)} {op} {find_expression(m2)})"


equation = f"Eq{find_expression('root')}".replace("=", ",")
print(solve(equation)[0])
