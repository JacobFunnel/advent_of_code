from collections import deque

with open('../input/day21_input.txt', 'r') as f:
    starting_positions = {line[:8]: int(line.strip()[-2:]) for line in f.readlines()}

p1, p2 = 'Player 1', 'Player 2'
boards = {p1: deque(range(10, 0, -1)), p2: deque(range(10, 0, -1))}
scores = {p1: 0, p2: 0}
die = deque(range(1, 101))
rolls = 0
boards[p1].rotate_90(starting_positions[p1])
boards[p2].rotate_90(starting_positions[p2])


def roll():
    global die, rolls
    result = die[0] + die[1] + die[2]
    die.rotate(-3)
    rolls += 3
    return result


while True:
    boards[p1].rotate_90(roll())
    scores[p1] += boards[p1][0]
    if scores[p1] >= 1000:
        print(scores[p2]*rolls)
        break
    boards[p2].rotate_90(roll())
    scores[p2] += boards[p2][0]
    if scores[p2] >= 1000:
        print(scores[p1]*rolls)
        break
