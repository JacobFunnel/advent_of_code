with open("input/08.txt", "r") as f:
    grid = [[int(n) for n in line] for line in f.read().splitlines()]

height, width = len(grid), len(grid[0])
visible = height * 2 + width * 2 - 4
for y in range(1, height - 1):
    for x in range(1, width - 1):
        tallest_in_sight = map(
            max,
            (
                grid[y][:x],
                grid[y][x + 1 :],
                [grid[h][x] for h in range(y)],
                [grid[h][x] for h in range(y + 1, height)],
            ),
        )

        if any(map(lambda a: a < grid[y][x], tallest_in_sight)):
            visible += 1

print(visible)
