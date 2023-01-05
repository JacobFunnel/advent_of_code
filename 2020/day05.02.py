with open("input/05.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    return [(line[:-3], line[-3:]) for line in lines]


def find_pos(seq):
    binary = "".join(["0" if char in "FL" else "1" for char in seq])
    return int(binary, 2)


def calculate_seats(lines):
    seats = []
    for r, c in lines:
        row = find_pos(r)
        col = find_pos(c)
        seats.append((row, col, row * 8 + col))
    return seats


seats = calculate_seats(parse(lines))
seat_numbers = sorted([seat[2] for seat in seats])

for i in range(seat_numbers[0], seat_numbers[-1]):
    if i not in seat_numbers:
        print(i)
