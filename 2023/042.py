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
card_totals = {card.idx: 1 for card in cards}

for card in cards:
    if wins := len(card.numbers.intersection(card.winning)):
        for idx in range(card.idx + 1, card.idx + wins + 1):
            card_totals[idx] += card_totals[card.idx]

print(sum(card_totals.values()))
