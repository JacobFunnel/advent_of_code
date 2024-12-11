from parse import parse_lines

grid = {(r, c): int(v) for r, row in enumerate(parse_lines()) for c, v in enumerate(row) if row}
trailheads = {p: 0 for p, elevation in grid.items() if elevation == 0}
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def score_trailhead(point):
    score = 0
    points = [point]
    while points:
        point = points.pop()
        if grid[point] == 9:
            score += 1
            continue
        points.extend(valid_neighbors(point))
    return score


def valid_neighbors(point):
    r, c = point
    return [
        (r + dr, c + dc) for dr, dc in DIRECTIONS if grid.get((r + dr, c + dc)) == grid[point] + 1
    ]


print(sum(score_trailhead(trailhead) for trailhead in trailheads))
