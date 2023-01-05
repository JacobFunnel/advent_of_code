with open("input/13.txt", "r") as f:
    pairs = [[eval(entry) for entry in pair.splitlines()] for pair in f.read().split("\n\n")]


def in_order(left, right):
    match left, right:
        case int(), int():
            return True if left < right else None if left == right else False
        case list(), list():
            for i in range(len(left)):
                try:
                    result = in_order(left[i], right[i])
                    if result is not None:
                        return result
                    else:
                        continue
                except IndexError:
                    return False
            if len(left) == len(right):
                return None
            else:
                return True
        case int(), list():
            return in_order([left], right)
        case list(), int():
            return in_order(left, [right])


indices_in_order = []
for idx, (left, right) in enumerate(pairs):
    if in_order(left, right):
        indices_in_order.append(idx + 1)
print(sum(indices_in_order))
