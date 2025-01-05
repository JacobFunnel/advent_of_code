import re

from parse import parse_all

a, b, c, *program = map(int, re.findall(r"\d+", parse_all()))
out = []
idx = 0


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
    global a, b, c, idx, out
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
        case 6:
            b = a // (2 ** combo(m))
        case 7:
            c = a // (2 ** combo(m))
    idx += 2

while True:
    try:
        instruction(program[idx], program[idx + 1])
    except IndexError:
        break

print(",".join(map(str,out)))
