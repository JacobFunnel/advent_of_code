import numpy as np

with open("input/10.txt", "r") as f:
    numbers = [[0 if x == "." else 1 for x in line.strip()] for line in f.readlines()]

asteroids = {complex(x, -y) for y, row in enumerate(numbers) for x, asteroid in enumerate(row) if
             asteroid}
asteroid_to_angles = {}
for asteroid in asteroids:
    others = asteroids ^ {asteroid}
    for other in others:
        angles = asteroid_to_angles.setdefault(asteroid, {})
        angles.setdefault(np.angle(other - asteroid, deg=True), []).append(other)

best_asteroid = max(asteroid_to_angles, key=lambda x: len(asteroid_to_angles.get(x)))
shifted_angles = {(-angle + 90) % 360: sorted(others, key=lambda x: abs(x - best_asteroid))
                  for angle, others in asteroid_to_angles[best_asteroid].items()}
shifted_angles = dict(sorted(shifted_angles.items()))


def find_nth_astroid(n):
    vaporized = []
    while True:
        for angle, others in shifted_angles.items():
            if others:
                vaporized.append(others.pop(0))
                if len(vaporized) == n:
                    nth = vaporized[-1]
                    return nth, abs(nth.real) * 100 + abs(nth.imag)


print(find_nth_astroid(200))
