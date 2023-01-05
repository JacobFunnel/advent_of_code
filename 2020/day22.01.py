with open("input/22.txt", "r") as f:
    players = f.read().split("\n\n")
    decks = {}
    for player, numbers in enumerate(players):
        decks[player] = [int(x) for x in numbers[10:].split("\n")]


def play(decks):
    while 0 not in list(map(len, decks.values())):
        cards = [decks[0].pop(0), decks[1].pop(0)]
        if cards[0] > cards[1]:
            decks[0].extend(cards)
        else:
            decks[1].extend(reversed(cards))

    if len(decks[0]) == 0:
        winning_deck = decks[1]
    else:
        winning_deck = decks[0]

    score_map = list(range(len(winning_deck), 0, -1))
    print(sum(x * y for x, y in zip(score_map, winning_deck)))


play(decks)
