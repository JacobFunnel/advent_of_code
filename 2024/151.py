from parse import parse_lines

grid, moves = parse_lines(2)
DIRECTIONS = {"^": -1, "v": 1, "<": -1j, ">": 1j}
moves = [DIRECTIONS[move] for line in moves.splitlines() for move in line if line]
positions = {}
grid = {(r + c * 1j): char for r, row in enumerate(grid.splitlines()) for c, char in enumerate(row)}
for pos, char in grid.items():
    positions.setdefault(char, set()).add(pos)

[robot_position], walls, boxes = positions["@"], positions["#"], positions["O"]

while moves:
    move = moves.pop(0)
    boxes_to_move = []
    new_position = robot_position
    while new_position := new_position + move:
        if new_position in walls:
            break
        if new_position in boxes:
            boxes_to_move.append(new_position)
            continue
        else:
            robot_position += move
            if boxes_to_move:
                boxes.remove(boxes_to_move[0])
                boxes.add(boxes_to_move[-1] + move)
            break

print(int(sum(box.real * 100 + box.imag for box in boxes)))
