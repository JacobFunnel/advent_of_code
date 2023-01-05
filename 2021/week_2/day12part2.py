with open('../input/day12_input.txt', 'r') as f:
    edges = {tuple(line.strip().split('-')) for line in f.readlines()}

nodes, small_caves, available_nodes = set(), set(), set()
start_edges = {edge for edge in edges if 'start' in edge}
end_edges = {edge for edge in edges if 'end' in edge}
paths = {1: ('start', )}
number_of_paths = 0
l = 1

for edge in edges:
    for node in edge:
        nodes.add(node)
        if node.isupper():
            pass
        elif len(node) == 2:
            small_caves.add(node)


def has_duplicate_small_caves(path):
    global small_caves
    small_cave_visits = {element: path.count(element) > 1 for element in path if element in small_caves}
    return True in small_cave_visits.values()


while True:
    l += 1
    paths[l] = set()
    if l == 2:
        for edge in start_edges:
            if edge[0] == 'start':
                path = (edge[0], edge[1])
            else:
                path = (edge[1], edge[0])
            paths[l].add(path)
    else:
        for path in paths[l-1]:
            if path[-1] != 'end':
                available_edges = {edge for edge in edges if path[-1] in edge}
                for edge in available_edges:
                    node = edge[0] if edge[0] != path[-1] else edge[1]
                    if node in small_caves:
                        if node not in path:
                            paths[l].add(path + (node,))
                        elif has_duplicate_small_caves(path):
                            pass
                        else:
                            paths[l].add(path + (node,))
                    elif node != 'start':
                        paths[l].add(path + (node, ))
    if len(paths[l]) == 0:
        print(l)
        break

for key in paths.keys():
    paths[key] = {path for path in paths[key] if 'end' in path}
    number_of_paths += len(paths[key])

print(number_of_paths)
