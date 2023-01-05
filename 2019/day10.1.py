import numpy as np

with open("input/10.txt", "r") as f:
    numbers = [[0 if x == "." else 1 for x in line.strip()] for line in f.readlines()]

asteroids = {complex(-x, -y) for y, row in enumerate(numbers) for x, asteroid in enumerate(row) if
             asteroid}
angles = {}

for asteroid in asteroids:
    others = asteroids ^ {asteroid}
    for other in others:
        angles[asteroid] = angles.setdefault(asteroid, set()) | {np.angle(asteroid - other)}

best_asteroid = max(angles, key=lambda x: len(angles.get(x)))
print(len(angles[best_asteroid]))
