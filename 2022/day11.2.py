import re
from collections import namedtuple

monkeys = []
Monkey = namedtuple("monkey", ["items", "formula", "div_by", "if_true", "if_false", "inspected"])

with open("input/11.txt", "r") as f:
    blocks = [block.splitlines()[1:] for block in f.read().split("\n\n")]
    for items, formula, div_by, if_true, if_false in blocks:
        items = list(map(int, re.findall(r'\d+', items)))
        formula = formula[formula.find("=") + 2:].split()
        div_by = int(div_by[div_by.rfind(" ") + 1:])
        if_true = int(if_true[if_true.rfind(" ") + 1:])
        if_false = int(if_false[if_false.rfind(" ") + 1:])
        monkeys.append(Monkey(items, formula, div_by, if_true, if_false, [0]))


def worry(x, operation, y, wlvl):
    operations = {"+": lambda a, b: a + b,
                  "*": lambda a, b: a * b}
    func = operations[operation]
    x = wlvl if x == "old" else int(x)
    y = wlvl if y == "old" else int(y)
    return func(x, y)


for _ in range(10000):
    for i, monkey in enumerate(monkeys):
        while monkey.items:
            item_wlvl = worry(*monkey.formula, monkey.items.pop(0))
            monkey.inspected[0] += 1
            if item_wlvl % monkey.div_by == 0:
                to_monkey = monkey.if_true
            else:
                to_monkey = monkey.if_false
            monkeys[to_monkey].items.append(item_wlvl)


a, b = sorted([monkey.inspected[0] for monkey in monkeys])[-2:]
print(a * b)
