from functools import reduce
from math import gcd


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def make_coprime(x, y):
    while True:
        factor = gcd(x, y)
        if factor == 1 or any([x == 0, y == 0]):
            return x, y
        else:
            x = int(x/factor)
            y = int(y/factor)


with open("input/13.txt", "r") as f:
    lines = f.read().split("\n")

buses = [entry for entry in lines[1].split(",")]
pairs = [(idx, int(time)) for idx, time in list(enumerate(buses)) if time != "x"]
# [(0, 37), (27, 41), (37, 457), (50, 13), (51, 17), (60, 23), (66, 29), (68, 431), (87, 19)]
coprime_pairs = [make_coprime(x, y) for x, y in pairs]
print(coprime_pairs)


a = [a for (a, y) in coprime_pairs]
n = [n for (x, n) in coprime_pairs]
print(a, n)
print(chinese_remainder(n, a))
