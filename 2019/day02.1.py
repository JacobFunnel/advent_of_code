with open("input/02.txt", "r") as f:
    numbers = [int(n) for n in f.read().split(",")]


ops = {1: lambda a, b: a + b, 2: lambda a, b: a * b, 99: False}
numbers[1] = 12
numbers[2] = 2
i = 0
while True:
    operation = ops[numbers[i]]
    if operation:
        numbers[numbers[i + 3]] = operation(numbers[numbers[i + 1]], numbers[numbers[i + 2]])
    else:
        break
    i += 4

print(numbers[0])
