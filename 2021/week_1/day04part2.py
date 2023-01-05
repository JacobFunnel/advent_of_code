import numpy as np

with open('../input/day04_input.txt', 'r') as f:
    in_put = f.readlines()

numbers_to_draw = [int(x) for x in in_put[0].strip().split(',')]
boards = []
bingo = []
bingo_numbers = {}
for i in range(0, len(in_put), 6):
    try:
        boards.append(np.mat([line.strip().split() for line in in_put[i + 2:i + 7]], dtype=int))
    except:
        break

boards.pop()
scores = [np.zeros(shape=(5, 5), dtype=int) for board in boards]


def is_bingo(number):
    for b in range(len(boards)):
        if b not in bingo:
            sums = np.append(scores[b].sum(axis=0), scores[b].sum(axis=1))
            if 5 in sums:
                bingo.append(b)
                bingo_numbers[b] = number
                return True


def play_bingo(number):
    for b in range(len(boards)):
        if b not in bingo and number in boards[b]:
            x, y = np.argwhere(boards[b] == number)[0]
            scores[b][x, y] = 1
            is_bingo(number)


for number in numbers_to_draw:
    play_bingo(number)

loser = bingo[-1]
unmarked_map = np.subtract(np.ones(shape=(5, 5), dtype=int), scores[loser])
unmarked_score = np.multiply(boards[loser], unmarked_map)
print(unmarked_score.sum()*bingo_numbers[loser])