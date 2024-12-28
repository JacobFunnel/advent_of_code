import networkx as nx

from parse import parse_lines


def any_start_with_t(nodes):
    return any(node.startswith("t") for node in nodes)


edges = (tuple(line.split("-")) for line in parse_lines()[:-1])
G = nx.Graph(edges)
cliques = [
    clique
    for clique in nx.enumerate_all_cliques(G)
    if len(clique) == 3 and any_start_with_t(clique)
]
print(len(cliques))
