from copy import deepcopy

with open("input/02.txt", "r") as f:
    input_numbers = [int(n) for n in f.read().split(",")]


ops = {1: lambda a, b: a + b, 2: lambda a, b: a * b, 99: False}


def find_inputs():
    for noun in range(100):
        for verb in range(100):
            numbers = deepcopy(input_numbers)
            numbers[1] = noun
            numbers[2] = verb
            i = 0
            while True:
                operation = ops[numbers[i]]
                if operation:
                    numbers[numbers[i + 3]] = operation(
                        numbers[numbers[i + 1]], numbers[numbers[i + 2]]
                    )
                else:
                    break
                i += 4
            if numbers[0] == 19690720:
                return 100 * noun + verb


print(find_inputs())
