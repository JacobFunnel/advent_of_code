with open("../input/day01_input.txt", "r") as f:
    measurements = f.read().split("\n")
    measurements.pop()
    measurements = [int(element) for element in measurements]

count = 0

for i in range(len(measurements) - 3):
    if sum(measurements[i + 1 : i + 3 + 1]) > sum(measurements[i : i + 3]):
        count += 1

print(count)
