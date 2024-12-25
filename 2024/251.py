from parse import parse_lines

locks_and_keys = parse_lines(2)
locks, keys = [], []
opposites = {".": "#", "#": "."}
length = 5
height = 7
for chunk in locks_and_keys:
    char = chunk[0]
    opposite = opposites[char]
    heights = [height - chunk.replace("\n", "")[n::length].index(opposite) for n in range(length)]
    if char == ".":
        keys.append(heights)
    else:
        locks.append(heights)

print(sum(1 for lock in locks for key in keys if all(k <= l for l, k in zip(lock, key))))
