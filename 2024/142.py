import re
from math import prod

import matplotlib.pyplot as plt

from parse import parse_lines


class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f"Robot({self.x}, {self.y}, {self.vx}, {self.vy})"

    def move(self, n=1):
        self.x = (self.x + self.vx * n) % 101
        self.y = (self.y + self.vy * n) % 103
        return self

    def quadrant(self):
        if self.x == 50 or self.y == 51:
            return 0
        elif self.x > 50:
            if self.y > 50:
                return 4
            else:
                return 3
        else:
            if self.y > 50:
                return 2
            else:
                return 1


robots = [
    Robot(*map(int, re.findall(r"-?\d+", line))).move(6870)
    for line in parse_lines()
    if line
]
print(prod(robots.count(n) for n in range(1,5)))


robots = [r.move() for r in robots]
plt.figure(figsize=(8, 8))
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Robot Positions')
plt.grid(True)
plt.show()
for n in range(6871, 50000):
    print(n)
    robots = [r.move() for r in robots]
    plt.scatter([r.x for r in robots], [r.y for r in robots], c='black', marker=',', s=2)
    plt.show()
