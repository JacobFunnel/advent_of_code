with open("input/16.txt", "r") as f:
    numbers = [int(n) for n in f.read().strip()]


def create_pattern(i):
    base_pattern = [0, 1, 0, -1]
    new_pattern = []
    for element in base_pattern:
        new_pattern.extend([element] * (i + 1))
    new_pattern.append(new_pattern.pop(0))
    return new_pattern


def generate_pattern(pattern):
    while True:
        for element in pattern:
            yield element


def next_phase(signal):
    length = len(signal)
    next_signal = []
    for i in range(length):
        pattern_generator = generate_pattern(create_pattern(i))
        pattern = [next(pattern_generator) for _ in range(length)]
        next_signal.append(abs(sum(x * y for x, y in zip(signal, pattern))) % 10)
    return next_signal


# for _ in range(100):
#     numbers = next_phase(numbers)

print("".join(str(n) for n in numbers * 1000))
