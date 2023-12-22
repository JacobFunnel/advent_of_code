with open("input/01.txt", "r") as f:
    supplies = [
        [int(supply) for supply in supplies.split("\n")] for supplies in f.read().split("\n\n")
    ]

supply_sums = [sum(supply) for supply in supplies]
print(max(supply_sums))
