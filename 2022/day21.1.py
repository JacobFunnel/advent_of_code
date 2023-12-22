with open("input/21.txt", "r") as f:
    monkeys = {line[:4]: line[6:].split() for line in f.read().splitlines()}

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def find_n(monkey):
    if len(monkeys[monkey]) == 1:
        n = int(monkeys[monkey][0])
        return n
    else:
        m1, op, m2 = monkeys[monkey]
        return operators[op](find_n(m1), find_n(m2))


print(int(find_n("root")))
