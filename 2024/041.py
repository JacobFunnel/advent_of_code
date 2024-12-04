import re

from parse import parse_lines

rows = [line for line in parse_lines() if line]
width, height = len(rows[0]), len(rows)
cols = ["".join([rows[j][i] for j in range(height)]) for i in range(width)]

def walk(r, c, dr, dc):
    diagonal = ""
    while r in range(height) and c in range(width):
        diagonal += rows[r][c]
        r += dr
        c += dc
    return diagonal


diagonals = []
for r in range(3, height):
    diagonals.append(walk(r=r, c=0, dr=-1, dc=1))
for c in range(1, width - 4):
    diagonals.append(walk(r=height - 1, c=c, dr=-1, dc=1))
for r in range(height - 4, -1, -1):
    diagonals.append(walk(r=r, c=0, dr=1, dc=1))
for c in range(1, width - 4):
    diagonals.append(walk(r=0, c=c, dr=1, dc=1))

print(
    sum(len(re.findall(r"XMAS", row)) for row in rows)
    + sum(len(re.findall(r"XMAS", row[::-1])) for row in rows)
    + sum(len(re.findall(r"XMAS", col)) for col in cols)
    + sum(len(re.findall(r"XMAS", col[::-1])) for col in cols)
    + sum(len(re.findall(r"XMAS", diagonal)) for diagonal in diagonals)
    + sum(len(re.findall(r"XMAS", diagonal[::-1])) for diagonal in diagonals)
)
