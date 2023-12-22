from math import trunc

with open("../input/day24_input.txt", "r") as f:
    instructions = [line.strip().split(" ") for line in f.readlines()]


def tryint(element):
    try:
        return int(element)
    except ValueError:
        return element


functions = {
    "add": lambda a, b: a + b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: trunc(a / b),
    "mod": lambda a, b: a % b,
    "eql": lambda a, b: 1 if a == b else 0,
}


def generate_model_nr():
    i = 99999999999999
    while True:
        if str(i).count("0") == 0:
            yield str(i)
            i -= 1
        else:
            i -= 1


def generate_digit(model_nr):
    for i in model_nr:
        yield int(i)


def monad(model_nr):
    digit_gen = generate_digit(model_nr)
    variables = {"w": 0, "x": 0, "y": 0, "z": 0}
    for line in instructions:
        if len(line) == 2:
            variables[line[1]] = next(digit_gen)
        else:
            instruction, a, b = line
            b = b if type(b) is int else variables[b]
            try:
                variables[a] = functions[instruction](variables[a], b)
            except ValueError:
                return False
    if variables["z"] == 0:
        return True
    else:
        return False


generator = generate_model_nr()
instructions = [[tryint(element) for element in line] for line in instructions]

while True:
    model_nr = next(generator)
    if monad(model_nr):
        print(model_nr)
        break
    else:
        print(f"{model_nr} not valid")
