with open("input/08.txt", "r") as f:
    grid = [[int(n) for n in line] for line in f.read().splitlines()]

height, width = len(grid), len(grid[0])
scenic_scores = []


def count_trees(h, line_of_sight):
    count = 0
    for tree in line_of_sight:
        if tree < h:
            count += 1
        elif tree >= h:
            return count + 1
    return count


for y in range(1, height - 1):
    for x in range(1, width - 1):
        l = count_trees(grid[y][x], reversed(grid[y][:x]))
        r = count_trees(grid[y][x], grid[y][x + 1 :])
        u = count_trees(grid[y][x], reversed([grid[h][x] for h in range(y)]))
        d = count_trees(grid[y][x], [grid[h][x] for h in range(y + 1, height)])
        scenic_scores.append(l * r * u * d)

print(max(scenic_scores))
