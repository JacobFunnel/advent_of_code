from parse import parse_lines

grid = [[char for char in line] for line in parse_lines() if line]
width, height = len(grid[0]), len(grid)
count = 0
for r in range(1, height - 1):
    for c in range(1, width - 1):
        if (grid[r][c] == "A" and
            {"S", "M"} == {grid[r - 1][c - 1], grid[r + 1][c + 1]} == {grid[r - 1][c + 1], grid[r + 1][c - 1]}):
            count += 1
print(count)
