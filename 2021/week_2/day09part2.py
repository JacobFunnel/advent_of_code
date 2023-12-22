import numpy as np

with open("../input/day09_input.txt", "r") as f:
    hmap = np.mat([[int(a) for a in line.strip()] for line in f.readlines()])

rows, columns = np.shape(hmap)
valid_nodes = {(i[0], i[1]) for i in np.argwhere(hmap != 9)}
basins = []


def neighbors(node):
    directions = {(1, 0), (0, 1), (-1, 0), (0, -1)}
    result = set()
    for direction in directions:
        neighbor = (node[0] + direction[0], node[1] + direction[1])
        if neighbor in valid_nodes:
            result.add(neighbor)
    return result


while valid_nodes:
    for node in valid_nodes:
        basin = {node}
        adjecent = neighbors(node)
        while True:
            search_space = adjecent - basin
            if search_space:
                basin |= adjecent
                adjecent.clear()
                for element in search_space:
                    adjecent |= neighbors(element)
            else:
                break

        basins.append(len(basin))
        valid_nodes -= basin
        break

print(np.prod(sorted(basins, reverse=True)[:3]))
