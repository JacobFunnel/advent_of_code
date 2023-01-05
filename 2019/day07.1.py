with open("input/07.txt", "r") as f:
    numbers = [int(n) for n in f.read().split("\n")]

print(sum([int(n / 3) - 2 for n in numbers]))
