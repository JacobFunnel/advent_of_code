from numpy.polynomial.hermite import poly2herm

from parse import parse_lines

grid, moves = parse_lines(2)
DIRECTIONS = {"^": -1, "v": 1, "<": -1j, ">": 1j}
moves = [DIRECTIONS[move] for line in moves.splitlines() for move in line if line]
grid = grid.replace(".", "..").replace("@", "@.").replace("O", "[]").replace("#", "##")

positions = {}
grid = {(r + c * 1j): char for r, row in enumerate(grid.splitlines()) for c, char in enumerate(row)}
for pos, char in grid.items():
    if char == "[":
        pos = (pos , pos + 1j)
    positions.setdefault(char, set()).add(pos)

[robot_position], walls, boxes = positions["@"], positions["#"], positions["["]


def draw():
    for r in range(8):
        for c in range(8):
            if (r + c * 1j) in walls:
                char = "#"
            elif (r + c * 1j) in boxes:
                char = "O"
            elif (r + c * 1j) == robot_position:
                char = "@"
            else:
                char = "."
            print(char, end="\n" if c == 7 else "")


def boxes_with_pos(pos):
    return [box for box in boxes if pos in box]


def affected_locations(box, move):
    p1, p2 = box
    return p1 + move, p2 + move

def move_box(box, move):
    p1, p2 = box
    new_box = (p1 + move, p2 + move)
    boxes.remove(box)
    boxes.add(new_box)


while moves:
    move = moves.pop(0)
    boxes_to_move = []
    new_position = robot_position
    while True:
        new_position += move
        if boxes_to_move and move.imag:
            new_position += move
        if new_position in walls:
            break
        if not boxes_to_move:
            if box_to_move := [box for box in boxes if new_position in box]:
                boxes_to_move.append(box_to_move)
                continue
        if boxes_to_move:
            new_positions = {pos + move for box in boxes_to_move[-1] for pos in box}
            if new_positions & walls:
                break
            else:
                boxes_to_move.append([box for box in boxes if set(box) & new_positions])
                continue
        else:
            robot_position += move
            if boxes_to_move:
                for boxes in boxes_to_move:
                    for box in boxes:
                        move_box(box, move)
            break

print(int(sum(min(p.real for p in box) * 100 + min(p.imag for p in box) for box in boxes)))
