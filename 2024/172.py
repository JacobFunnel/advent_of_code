import re

from parse import parse_all

a, b, c, *program = map(int, re.findall(r"\d+", parse_all()))


def combo(op):
    if op <= 3:
        return op
    elif op == 4:
        return a
    elif op == 5:
        return b
    elif op == 6:
        return c


def instruction(n, m):
    global a, b, c, idx, out, fail
    match n:
        case 0:
            a = a // (2 ** combo(m))
        case 1:
            b ^= m
        case 2:
            b = combo(m) % 8
        case 3:
            if a != 0:
                idx = m
                return
        case 4:
            b ^= c
        case 5:
            out.append(combo(m) % 8)
            if not all(a == b for a, b in zip(out, program)):
                fail = True
                return

        case 6:
            b = a // (2 ** combo(m))
        case 7:
            c = a // (2 ** combo(m))
    idx += 2

new_a = 0
while True:
    new_a += 1
    a = new_a
    idx = 0
    out = []
    fail = False
    while True:
        try:
            instruction(program[idx], program[idx + 1])
            if fail:
                break
        except IndexError:
            break
    if not fail and out == program:
        break

print(f"{new_a=}")
print(",".join(map(str, out)))
