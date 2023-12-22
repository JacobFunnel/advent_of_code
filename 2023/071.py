from parse import parse_lines
from collections import defaultdict, namedtuple

hands = {line.split()[0]: int(line.split()[-1]) for line in parse_lines()}
card_ranking = "AKQJT98765432"


def score_card(card):
    return card_ranking.index(card)


def score_hand(hand):
    card_amounts = defaultdict(int)
    for card in hand:
        card_amounts[card] += 1
    most_of_a_kind = max(card_amounts.values())
    if most_of_a_kind == 5:
        hand_score = 1  # 5 of a kind
    elif most_of_a_kind == 4:
        hand_score = 2  # 4 of a kind
    elif most_of_a_kind == 3:
        if 2 in card_amounts.values():
            hand_score = 3  # full house
        else:
            hand_score = 4  # 3 of a kind
    elif most_of_a_kind == 2:
        number_of_pairs = list(card_amounts.values()).count(2)
        if number_of_pairs == 2:
            hand_score = 5  # 2 pair
        else:
            hand_score = 6  # 1 pair
    else:
        hand_score = 7  # high card
    return hand_score


hands = {
    hand: namedtuple("hand_values", ["hand_score", "card_scores", "bid"])(
        score_hand(hand), [score_card(c) for c in hand], bid
    )
    for hand, bid in hands.items()
}


def rank_hands(hands):
    return sorted(
        hands.keys(),
        key=lambda h: (hands[h].hand_score, hands[h].card_scores),
        reverse=True,
    )


sorted_hands = rank_hands(hands)
sorted_bids = [hands[hand].bid for hand in sorted_hands]
print(sum(rank * bid for rank, bid in (zip(range(1, len(sorted_bids) + 1), sorted_bids))))
