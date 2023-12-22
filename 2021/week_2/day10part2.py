with open("../input/day10_input.txt", "r") as f:
    lines = {line.strip() for line in f.readlines()}

match = {"}": "{", "]": "[", ")": "(", ">": "<", "{": "}", "[": "]", "(": ")", "<": ">"}
opening = {"{", "[", "(", "<"}
scoremap = {"}": 3, "]": 2, ")": 1, ">": 4}
closers = []
scores = []

for line in lines:
    opened = []
    corrupted = False
    for bracket in line:
        if bracket in opening:
            opened.append(bracket)
        else:
            if opened[-1] == match[bracket]:
                opened.pop()
            else:
                corrupted = True
                break
    if not corrupted:
        closers.append([match[bracket] for bracket in reversed(opened)])

for closer in closers:
    score = 0
    for bracket in closer:
        score = 5 * score + scoremap[bracket]
    scores.append(score)

print(sorted(scores)[int(len(scores) / 2)])
