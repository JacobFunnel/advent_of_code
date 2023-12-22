with open("input/08.txt", "r") as f:
    numbers = [int(n) for n in f.read().strip()]

layers = []
for i in range(0, len(numbers), 25 * 6):
    window = numbers[i : i + 25 * 6]
    layers.append((window.count(0), window.count(1) * window.count(2)))

print(sorted(layers, key=lambda t: t[0])[0][1])
