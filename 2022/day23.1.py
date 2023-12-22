with open("input/23.txt", "r") as f:
    elves = {
        (x, y)
        for y, line in enumerate(f.read().splitlines())
        for x, char in enumerate(line)
        if char == "#"
    }

direction_groups = [
    ["N", "NE", "NW"],
    ["S", "SE", "SW"],
    ["W", "NW", "SW"],
    ["E", "NE", "SE"],
]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def rotate_direction_groups():
    global direction_groups
    direction_groups.append(direction_groups.pop(0))


def propose_move(elf):
    global proposed
    directions = {
        "E": (1, 0),
        "N": (0, 1),
        "W": (-1, 0),
        "S": (0, -1),
        "NE": (1, 1),
        "SW": (-1, -1),
        "SE": (1, -1),
        "NW": (-1, 1),
    }
    if not elves ^ {add(elf, d) for d in directions.values()}:
        return
    else:
        for directions_to_check in direction_groups:
            if all(add(elf, directions[d]) not in elves for d in directions_to_check):
                proposed[elf] = add(elf, directions[directions_to_check[0]])
                break


def take_turn():
    global elves
    for elf in elves:
        propose_move(elf)
    proposed_destinations = list(proposed.values())
    valid_proposals = {k: v for k, v in proposed.items() if proposed_destinations.count(v) == 1}
    elves = (elves - set(valid_proposals.keys())) | set(valid_proposals.values())
    rotate_direction_groups()


for _ in range(5):
    proposed = {}
    take_turn()
    print(elves)
