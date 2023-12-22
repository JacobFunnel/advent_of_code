with open("input/02.txt", "r") as f:
    pairs = [tuple(pair.split()) for pair in f.readlines()]


def rps(pair):
    outcomes = {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,
        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 6,
    }
    shapes = {"X": 1, "Y": 2, "Z": 3}
    return outcomes[pair] + shapes[pair[-1]]


score = 0
for pair in pairs:
    score += rps(pair)

print(score)
