import networkx as nx

from parse import parse_lines

edges = (tuple(line.split("-")) for line in parse_lines()[:-1])
G = nx.Graph()
G.add_edges_from(edges)
cliques = []
for clique in nx.find_cliques(G):
    if len(clique) == 3:
        # if any(node.startswith("t") for node in clique):
        cliques.append(clique)

print(list(nx.connected_components(G)))
print([len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)])