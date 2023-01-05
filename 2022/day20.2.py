with open("input/20.txt", "r") as f:
    numbers = [(int(line) * 811589153, identity)
               for identity, line in enumerate(f.read().splitlines())]


def wrap(idx, n, l):
    naive = idx + n
    wraps = naive//l
    result = naive % l + wraps
    while result not in range(l):
        wraps = result//l
        result = result % l + wraps
    return result


l = len(numbers)
for mix in range(10):
    for identity in range(l):
        idx = numbers.index([(n, i) for n, i in numbers if i == identity][0])
        n, _ = numbers[idx]
        where = wrap(idx, n, l)
        if where != 0:
            numbers.insert(where, numbers.pop(idx))
        else:
            numbers.append(numbers.pop(idx))

numbers = [n for n, i in numbers]
a = numbers[(numbers.index(0) + 1000) % l]
b = numbers[(numbers.index(0) + 2000) % l]
c = numbers[(numbers.index(0) + 3000) % l]
print(a, b, c, a + b + c)
