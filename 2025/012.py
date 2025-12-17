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
    password += sum(
        1
        for d in range(position, position + rotation, rotation // abs(rotation))
        if d % 100 == 0
    )
    position = (position + rotation) % 100

print(password)
