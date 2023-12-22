from copy import deepcopy

with open("input/08.txt", "r") as f:
    lines = f.read().split("\n")

acc = 0


def parse(lines):
    return [[line[:3], int(line[4:])] for line in lines]


def execute_instruction(instruction, idx):
    global acc
    op, value = instruction
    if op == "acc":
        acc += value
        return idx + 1
    elif op == "jmp":
        return idx + value
    elif op == "nop":
        return idx + 1


def valid_program(instructions):
    global acc
    acc = 0
    idx = 0
    visited_indices = []
    while True:
        if idx == len(instructions):
            print(f"Success! Acc: {acc}")
            return True
        try:
            idx = execute_instruction(instructions[idx], idx)
        except IndexError:
            return False
        if idx not in visited_indices:
            visited_indices.append(idx)
        else:
            return False


instructions = parse(lines)
flip_indices = []
for i, (op, value) in enumerate(instructions):
    if op in {"nop", "jmp"}:
        flip_indices.append(i)


def flip(op):
    return "nop" if op == "jmp" else "jmp"


for i in flip_indices:
    new_instr = deepcopy(instructions)
    op, value = new_instr[i]
    new_instr[i] = [flip(op), value]
    if valid_program(new_instr):
        break
