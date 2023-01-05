from collections import deque

with open("input/23.txt", "r") as f:
    cups = deque([int(x) for x in f.read()])
    cups.extend(list(range(10, 1000001)))


def find_destination_idx():
    global cups
    n = -1
    while True:
        seeked = (cups[-1] + n) % 10
        if seeked in cups and seeked != cups[-1]:
            destination_idx = cups.index(seeked)
            break
        else:
            n -= 1
    return destination_idx


def find_next(current_cup):
    global cups
    return cups.index(current_cup) + 1 % 9


def make_moves(n):
    for i in range(n):
        cups.rotate(-1)
        current_cup = cups[-1]
        picked_up = [cups.popleft() for x in range(1, 4)]
        cups.rotate(-find_destination_idx() - 1)
        cups.extend(picked_up)
        cups.rotate(-find_next(current_cup))


make_moves(10000000)
cups.rotate(find_next(1))
print(cups[1] * cups[2])
