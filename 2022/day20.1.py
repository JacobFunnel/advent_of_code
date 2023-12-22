with open("input/20.txt", "r") as f:
    numbers = [(int(line), identity) for identity, line in enumerate(f.read().splitlines())]


def wrap(idx, n, l):
    naive = idx + n
    wraps = naive // l
    return (idx + n) % l + wraps


l = len(numbers)
for identity in range(l):
    idx = numbers.index([(n, i) for n, i in numbers if i == identity][0])
    n, _ = numbers[idx]
    where = wrap(idx, n, l)
    if where != 0:
        numbers.insert(where, numbers.pop(idx))
    else:
        numbers.append(numbers.pop(idx))

numbers = [n for n, i in numbers]
print(
    numbers[(numbers.index(0) + 1000) % l]
    + numbers[(numbers.index(0) + 2000) % l]
    + numbers[(numbers.index(0) + 3000) % l]
)
