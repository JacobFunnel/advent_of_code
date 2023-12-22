with open("../input/day03_input.txt", "r") as f:
    measurements = f.read().split("\n")

measurements.pop()
length = len(measurements[0])
ones = [0] * length
zeroes = [0] * length

for i in range(length):
    for measurement in measurements:
        if measurement[i] == "1":
            ones[i] += 1
        else:
            zeroes[i] += 1

gamma = "".join(["1" if ones[i] > zeroes[i] else "0" for i in range(length)])
epsilon = "".join(["1" if ones[i] < zeroes[i] else "0" for i in range(length)])

print(int(gamma, 2) * int(epsilon, 2))
