with open("input/06.txt", "r") as f:
    pairs = [(line[:3], line[4:]) for line in f.read().split("\n")]


def build_tree(center):
    return {center: build_tree(o) for c, o in pairs if c == center} or center


trees = []
print(build_tree("COM"))
c_counts, o_counts = {}, {}
for c, o in pairs:
    c_counts[c] = c_counts.setdefault(c, 0) + 1
    o_counts[o] = o_counts.setdefault(o, 0) + 1

root_centers = []
for c in c_counts.keys():
    if c not in o_counts:
        root_centers.append(c)

counts = {}
for planet in [a for a, b in pairs] + [b for a, b in pairs]:
    counts[planet] = counts.setdefault(planet, 0) + 1



