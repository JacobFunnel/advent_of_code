with open("../input/day23_input.txt", "r") as f:
    pass

steps = {"a": 0, "b": 0, "c": 0, "d": 0}
cost = {"a": 1, "b": 10, "c": 100, "d": 1000}
energy = 0

steps["a"] += 2 + 3
steps["a"] += 8 + 9
steps["d"] += 7 + 7
steps["c"] += 2
steps["b"] += 6 + 4
steps["c"] += 3 + 7

for key, value in steps.items():
    energy += cost[key] * value

print(energy)
