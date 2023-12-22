start, end = None, None


def height(x, y, c):
    global start, end
    if c == "S":
        start = (x, y)
        return 0
    elif c == "E":
        end = (x, y)
        return 25
    else:
        return ord(c) - 97


with open("input/12.txt", "r") as f:
    grid = [
        [height(x, y, c) for x, c in enumerate(line)]
        for y, line in enumerate(f.read().splitlines())
    ]

print(grid, start, end)
