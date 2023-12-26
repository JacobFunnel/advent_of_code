from parse import parse_lines


grid = [[char for char in line] for line in parse_lines()]
start = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"][0]
plots = {(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char in (".", "S")}
cardinals = ((0, 1), (0, -1), (1, 0), (-1, 0))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neighboring_plots(node):
    return {add(node, cardinal) for cardinal in cardinals} & plots


def take_steps(n):
    positions = {start}
    for _ in range(n):
        new_positions = set()
        for position in positions:
            new_positions |= neighboring_plots(position)
        positions = new_positions
    return len(positions)


print(take_steps(64))
