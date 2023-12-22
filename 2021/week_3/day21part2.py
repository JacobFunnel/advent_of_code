import time

start_time = time.time()
with open("../input/day21_input.txt", "r") as f:
    starting_positions = {line[:8]: int(line.strip()[-2:]) for line in f.readlines()}

p1, p2 = "Player 1", "Player 2"
die_rolls = set()

for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            die_rolls.add((a, b, c))

results = {die_roll: sum(die_roll) for die_roll in die_rolls}
wins = {p1: 0, p2: 0}
scores = wins.copy()
universes = {outcome: list(results.values()).count(outcome) for outcome in set(results.values())}
nest = universes.copy()


def turn_board(board, die):
    board = (board + die) % 10
    return board or 10


def nested_dicts(obj):
    global wins
    multiplier, player, scores, boards, nested = obj
    for die, value in nested.items():
        if type(value) is int and value:
            next_boards = boards.copy()
            next_boards[player] = turn_board(boards[player], die)
            next_scores = scores.copy()
            next_scores[player] += next_boards[player]
            next_player = p1 if player == p2 else p2
            next_multiplier = multiplier * value
            if next_scores[player] >= 21:
                wins[player] += next_multiplier
                nested[die] = 0
            else:
                nested[die] = nested_dicts(
                    (
                        next_multiplier,
                        next_player,
                        next_scores,
                        next_boards,
                        nest.copy(),
                    )
                )
        if type(value) is tuple:
            nested[die] = nested_dicts(value)
    nested = {key: value for key, value in nested.items() if value != 0}
    return multiplier, player, scores, boards, nested


universes = (1, p1, scores.copy(), starting_positions, universes.copy())
universes = nested_dicts(universes)
print(wins)
print(time.time() - start_time)
