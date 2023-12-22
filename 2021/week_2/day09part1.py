import numpy as np

with open("../input/day09_input.txt", "r") as f:
    input_nested_list = [[int(a) for a in line.strip()] for line in f.readlines()]

hmap = np.mat(input_nested_list)
a, b = np.shape(hmap)
lowpoints = np.zeros(shape=(a, b), dtype=int)


def lowest(matrix, x, y):
    a, b = np.shape(matrix)
    neighbours = []
    if 0 <= x < a and 0 <= y - 1 < b:
        neighbours.append(matrix[x, y - 1])
    if 0 <= x < a and 0 <= y + 1 < b:
        neighbours.append(matrix[x, y + 1])
    if 0 <= x - 1 < a and 0 <= y < b:
        neighbours.append(matrix[x - 1, y])
    if 0 <= x + 1 < a and 0 <= y < b:
        neighbours.append(matrix[x + 1, y])
    return 1 if matrix[x, y] < min(neighbours) else 0


for x in range(a):
    for y in range(b):
        lowpoints[x, y] = lowest(hmap, x, y)

print(np.sum(np.multiply(hmap, lowpoints)) + np.sum(lowpoints))
