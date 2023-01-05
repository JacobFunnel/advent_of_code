with open("input/08.txt", "r") as f:
    lines = f.read().split("\n")

acc = 0


def parse(lines):
    return [(line[:3], int(line[4:])) for line in lines]


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


def find_loop(instructions):
    global acc
    idx = 0
    visited_indices = set()
    while True:
        idx = execute_instruction(instructions[idx], idx)
        if idx not in visited_indices:
            visited_indices.add(idx)
        else:
            print(acc)
            break


find_loop(parse(lines))
