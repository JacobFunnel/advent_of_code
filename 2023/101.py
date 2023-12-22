import math
from parse import parse_lines

grid = [[c for c in line] for line in parse_lines()]
r_max = len(grid) - 1
c_max = len(grid[0]) - 1
directions = {(-1, 0): (1, 0), (1, 0): (-1, 0), (0, -1): (0, 1), (0, 1): (0, -1)}
pipe_types = {
    "S": directions,
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
}


def valid_node(node):
    r, c = node
    return 0 <= r <= r_max and 0 <= c <= c_max


class Pipe:
    def __init__(self, node, shape):
        self.node = node
        self.shape = shape
        if shape == "S":
            self.start = True
            self.open_towards = {add(self.node, d) for d in directions}
        else:
            self.start = False
            self.open_towards = tuple(add(self.node, d) for d in pipe_types[shape])

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.node == other.node

    def __repr__(self):
        return (
            f"Pipe(node={self.node}, shape={self.shape}, "
            f"open_towards={self.open_towards}, start={self.start})"
        )


def find_neighbors(node):
    return filter(valid_node, (add(node, d) for d in directions))


def add(node, delta):
    r, c = node
    d_r, d_c = delta
    return r + d_r, c + d_c


def find_loop():
    pipes = []
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "S":
                start_pipe = Pipe((r, c), "S")
                pipes.append(start_pipe)
                while True:
                    pipe = pipes[-1]
                    for r1, c1 in find_neighbors(pipe.node):
                        shape = grid[r1][c1]
                        if shape in pipe_types:
                            neighbor = Pipe((r1, c1), shape)
                            if (
                                pipe.node in neighbor.open_towards
                                and neighbor.node in pipe.open_towards
                            ):
                                if neighbor not in pipes:
                                    pipes.append(neighbor)
                                    break
                                elif neighbor.start and len(pipes) > 2:
                                    return pipes


pipes = find_loop()
print(math.ceil(len(pipes) / 2))
