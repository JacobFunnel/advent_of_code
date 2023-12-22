from parse import parse_lines
from collections import namedtuple

Card = namedtuple("Card", ["idx", "winning", "numbers"])
cards = [
    Card(
        int(line.split(": ")[0].split()[-1]),
        {int(n) for n in line.split(": ")[-1].split(" | ")[0].split()},
        {int(n) for n in line.split(": ")[-1].split(" | ")[-1].split()},
    )
    for line in parse_lines()
]
total = 0
for card in cards:
    if wins := len(card.numbers.intersection(card.winning)):
        total += 2 ** (wins - 1)

print(total)
