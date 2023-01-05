with open("input/01.txt", "r") as f:
    supplies = [[int(supply) for supply in supplies.split("\n")] for supplies in
                f.read().split("\n\n")]

supply_sums = sorted([sum(supply) for supply in supplies], reverse=True)
print(sum(supply_sums[:3]))
