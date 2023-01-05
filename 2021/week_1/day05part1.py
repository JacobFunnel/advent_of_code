lines = []
with open('../input/day05_input.txt', 'r') as f:
    while True:
        try:
            pos1, pos2 = f.readline().strip().split(' -> ')
            (x1, y1), (x2, y2) = pos1.split(','), pos2.split(',')
            lines.append((int(x1), int(y1), int(x2), int(y2)))
        except:
            break

matrix = [[0 for x in range(1000)] for y in range(1000)]

for line in lines:
    x1, y1, x2, y2 = line
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            matrix[x1][y] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            matrix[x][y1] += 1
    else:
        pass

count = 0
for x in range(1000):
    for y in range(1000):
        if matrix[x][y] > 1:
            count += 1

print(count)
