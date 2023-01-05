from collections import deque

with open("input/15.txt", "r") as f:
    initial_numbers = [int(n) for n in f.read().split(",")]


def next_number(initial_numbers, max_turns=30000000):
    recently_spoken = {n: deque([idx + 1], maxlen=2) for idx, n in enumerate(initial_numbers)}
    last_spoken = initial_numbers[-1]
    turn = len(initial_numbers)
    while turn < max_turns:
        turn += 1
        if len(recently_spoken[last_spoken]) == 1:
            next_spoken = 0
        else:
            next_spoken = recently_spoken[last_spoken][-1] - recently_spoken[last_spoken][0]
        recently_spoken.setdefault(next_spoken, deque([], maxlen=2)).append(turn)
        last_spoken = next_spoken
    return last_spoken


print(next_number(initial_numbers))
