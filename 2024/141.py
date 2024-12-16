import re
from math import prod

from parse import parse_lines


class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f"Robot({self.x}, {self.y}, {self.vx}, {self.vy})"

    def move(self, n):
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
    Robot(*map(int, re.findall(r"-?\d+", line))).move(100).quadrant()
    for line in parse_lines()
    if line
]
print(prod(robots.count(n) for n in range(1,5)))
