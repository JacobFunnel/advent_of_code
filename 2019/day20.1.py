import re


def parse():
    with open("input/20.txt", "r") as f:
        char_grid = [[char for char in line] for line in f.readlines()]
        maze = {}
        for y, line in enumerate(f.readlines()):
            for x, char in enumerate(line):
                if re.match(r"\.|[A-Z]", char):
                    maze[char] = maze.setdefault(char, set()) | {(x, y)}
        return maze


def neighborhood(pos):
    x, y = pos
    combos = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
    return {(x + v, y + w) for v, w in combos}


def find_portals(maze):
    portals, non_portals = {}, {}
    connections = []
    for char in maze.keys():
        if char != ".":
            for pos in maze[char]:
                if maze_points := neighborhood(pos).intersection(maze["."]):
                    portals[pos] = (char, list(maze_points)[0])
                else:
                    non_portals[pos] = char

    for pos in portals.keys():
        k = list(neighborhood(pos).intersection(set(non_portals.keys())))[0]
        connections.append((pos, *portals[pos], k, non_portals[k]))

    return connections


print(find_portals(parse()))
