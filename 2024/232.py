import networkx as nx

from parse import parse_lines


edges = (tuple(line.split("-")) for line in parse_lines()[:-1])
G = nx.Graph(edges)
print(",".join(sorted(max(nx.find_cliques(G), key=len))))
