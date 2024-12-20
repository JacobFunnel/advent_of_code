from parse import parse_lines

grid, moves = parse_lines(2)
DIRECTIONS = {"^": -1, "v": 1, "<": -1j, ">": 1j}
moves = [DIRECTIONS[move] for line in moves.splitlines() for move in line if line]
grid = grid.replace(".", "..").replace("@", "@.").replace("O", "[]").replace("#", "##")
grid = {(r + c * 1j): char for r, row in enumerate(grid.splitlines()) for c, char in enumerate(row)}
width, height = int(max(grid, key=lambda p: p.imag).imag + 1), int(max(grid, key=lambda p: p.real).real + 1)
positions = {}
for pos, char in grid.items():
    if char == "[":
        pos = (pos , pos + 1j)
    positions.setdefault(char, set()).add(pos)

[robot_position], walls, boxes = positions["@"], positions["#"], positions["["]


def draw():
    bracket = True
    brackets = {True: "[", False: "]"}
    for r in range(height):
        for c in range(width):
            if (r + c * 1j) in walls:
                char = "#"
            elif [box for box in boxes if (r + c * 1j) in box]:
                char = brackets[bracket]
                bracket = not bracket
            elif (r + c * 1j) == robot_position:
                char = "@"
            else:
                char = "."
            print(char, end="\n" if c == width - 1 else "")


def move_boxes(queue, move):
    global boxes
    old_box_positions = {box for line in queue for box in line}
    new_box_positions = {(p1 + move, p2 + move) for p1, p2 in old_box_positions}
    boxes -= old_box_positions
    boxes |= new_box_positions


move = None
n = 0
while moves:
    # if move:
    #     print("Move ", n, " ", {v: k for k, v in DIRECTIONS.items()}[move], ":")
    # draw()
    n += 1
    # input("next?")
    move = moves.pop(0)
    boxes_to_move = []
    new_position = robot_position
    while True:
        new_position += move
        if boxes_to_move and move.imag:
            # look ahead another step if moving boxes horizontally
            new_position += move
        if new_position in walls:
            break
        if not boxes_to_move or move.imag:
            if box_to_move := [box for box in boxes if new_position in box]:
                boxes_to_move.append(box_to_move)
                continue
        if boxes_to_move and not move.imag:
            new_positions = {pos + move for box in boxes_to_move[-1] for pos in box}
            if new_positions & walls:
                break
            else:
                if more_boxes_to_move := [box for box in boxes if set(box) & new_positions]:
                    boxes_to_move.append(more_boxes_to_move)
                    continue
                else:
                    robot_position += move
                    move_boxes(boxes_to_move, move)
                    break
        else:
            robot_position += move
            move_boxes(boxes_to_move, move)
            break

draw()
print(n)
print(int(sum(min(p.real for p in box) * 100 + min(p.imag for p in box) for box in boxes)))
