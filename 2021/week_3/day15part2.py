import numpy as np

with open('../input/day15_input.txt', 'r') as f:
    grid = np.mat([list(map(int, list(line.strip()))) for line in f.readlines()], dtype=int)

big_grid = np.concatenate((grid, grid + 1, grid + 2, grid + 3, grid + 4), axis=1)
for i in range(4):
    big_grid = np.concatenate(
        (big_grid,
         np.concatenate((grid + i + 1, grid + i + 2, grid + i + 3, grid + i + 4, grid + i + 5), axis=1)),
        axis=0)
big_grid = big_grid % 9
big_grid = np.where(big_grid == 0, 9, big_grid)

all_nodes = set()
all_edges = {}
rows, columns = np.shape(big_grid)

for x in range(rows):
    for y in range(columns):
        all_nodes.add((x, y))


def edge_builder(node):
    directions = {(1, 0), (0, 1), (-1, 0), (0, -1)}
    neighbords = set()
    edges = {}
    for direction in directions:
        neighbor = (node[0] + direction[0], node[1] + direction[1])
        if neighbor in all_nodes:
            neighbords.add(neighbor)
            edges[(node, neighbor)] = big_grid[neighbor]
            edges[(neighbor, node)] = big_grid[node]
    return edges


for node in all_nodes:
    all_edges.update(edge_builder(node))


def dijkstra(unvisited, start, end):
    distances = {node: float('inf') for node in unvisited}
    distances[start] = 0
    while True:
        node = min({key: value for key, value in distances.items() if key in unvisited}, key=distances.get)
        edge_lengths = {edge: all_edges[edge] for edge in all_edges if edge[1] in unvisited and node == edge[0]}
        for (a, b) in edge_lengths:
            distances[b] = min(distances[b], all_edges[(a, b)] + distances[node])
        unvisited -= {node}
        if end not in unvisited or min(distances.values()) == float('inf'):
            break

    return distances[end]


print(dijkstra(all_nodes, (0, 0), (rows - 1, columns - 1)))
