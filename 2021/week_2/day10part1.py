with open("../input/day10_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

match = {"}": "{", "]": "[", ")": "(", ">": "<"}
opening = {"{", "[", "(", "<"}
opened = []
scores = {"}": 1197, "]": 57, ")": 3, ">": 25137}
score = 0

for line in lines:
    for bracket in line:
        if bracket in opening:
            opened.append(bracket)
        else:
            if opened[-1] == match[bracket]:
                opened.pop()
            else:
                score += scores[bracket]
                break

print(score)
