with open("input/01.txt", "r") as f:
    numbers = [int(n) for n in f.read().split("\n")]

all_fuel = 0
for n in numbers:
    fuel = n
    while True:
        fuel = int(fuel / 3) - 2
        if fuel > 0:
            all_fuel += fuel
        else:
            break

print(all_fuel)
