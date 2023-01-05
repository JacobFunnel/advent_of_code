with open("input/05.txt", "r") as f:
    numbers = [int(n) for n in f.read().split(",")]


ops = {"01": lambda a, b: a + b, "02": lambda a, b: a * b, "99": False}
print(numbers)
