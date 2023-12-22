import re

with open("input/05.txt", "r") as f:
    raw_stacks, raw_moves = f.read().split("\n\n")

transposed = list(zip(*raw_stacks.splitlines()[:-1]))[1::4]
stacks = {i + 1: [char for char in line[::-1] if char != " "] for i, line in enumerate(transposed)}
moves = [tuple(map(int, re.findall(r"\d+", line))) for line in raw_moves.splitlines()]

for amount, fr, to in moves:
    stacks[to].extend([stacks[fr].pop() for _ in range(amount)])

print("".join(stack[-1] for stack in stacks.values()))
