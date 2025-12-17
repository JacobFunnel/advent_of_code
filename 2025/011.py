from parse import parse_lines

DIRECTIONS = {
    "L": -1,
    "R": 1,
}
rotations = [
    (DIRECTIONS[direction] * int("".join(digits)))
    for direction, *digits in parse_lines()
]
position = 50
password = 0
for rotation in rotations:
    position = (position + rotation) % 100
    if position == 0:
        password += 1
print(password)
