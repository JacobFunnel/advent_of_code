with open("input/02.txt", "r") as f:
    pairs = [tuple(pair.split()) for pair in f.readlines()]

win_map = {"A": "C", "B": "A", "C": "B"}
lose_map = {v: k for k, v in win_map.items()}
outcomes = {("A", "X"): 6, ("A", "Y"): 3, ("A", "Z"): 0,
            ("B", "X"): 6, ("B", "Y"): 3, ("B", "Z"): 0,
            ("C", "X"): 6, ("C", "Y"): 3, ("C", "Z"): 0}
shapes = {"A": 1, "B": 2, "C": 3}


def rps(pair):
    return outcomes[pair] + shapes[find_shape(pair)]


def find_shape(pair):
    opponent, you = pair
    if you == "X":
        return win_map[opponent]
    elif you == "Y":
        return opponent
    elif you == "Z":
        return lose_map[opponent]


score = 0
for pair in pairs:
    score += rps(pair)

print(score)
