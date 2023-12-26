from parse import parse_lines


grid = [[char for char in line] for line in parse_lines()]
max_r_idx = len(grid)
max_c_idx = len(grid[0])
start = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"][0]
plots = {(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char in (".", "S")}
cardinals = ((0, 1), (0, -1), (1, 0), (-1, 0))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mod(a):
    return a[0] % max_r_idx, a[1] % max_c_idx


def neighboring_plots(node):
    return {add(node, cardinal) for cardinal in cardinals if mod(add(node, cardinal)) in plots}


def take_steps(n):
    positions = {start}
    for i in range(n):
        new_positions = set()
        for position in positions:
            new_positions |= neighboring_plots(position)
        positions = new_positions
    return len(positions)


print(take_steps(26501365))
#  way too slow, requires way too much memory
