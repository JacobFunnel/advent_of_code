with open("../input/day23_input.txt", "r") as f:
    pass

visited = {"a": 0, "b": 0, "c": 0, "d": 0}
cost = {"a": 1, "b": 10, "c": 100, "d": 1000}
energy = 0

visited["a"] += 2 + 3
visited["a"] += 8 + 9
visited["d"] += 7 + 7
visited["c"] += 2
visited["b"] += 6 + 4
visited["c"] += 3 + 7

for key, value in visited.items():
    energy += cost[key] * value

print(energy)
