with open("input/22.txt", "r") as f:
    players = f.read().split("\n\n")
    decks = {}
    for player, numbers in enumerate(players):
        decks[player] = [int(x) for x in numbers[10:].split("\n")]


def play(decks):
    while 0 not in list(map(len, decks.values())):
        cards = [decks[0].pop(0), decks[1].pop(0)]
        if cards[0] <= len(decks[0]) and cards[1] <= len(decks[1]):
            winner, winning_deck = play(decks)
        else:
            if cards[0] > cards[1]:
                winner = 0
            else:
                winner = 1
        if winner == 0:
            decks[0].extend(cards)
        else:
            decks[1].extend(reversed(cards))

    if len(decks[0]) == 0:
        winner = 1
    else:
        winner = 0
    return winner, decks[winner]


winner, winning_deck = play(decks)
score_map = list(range(len(winning_deck), 0, -1))
print(sum(x * y for x, y in zip(score_map, winning_deck)))
