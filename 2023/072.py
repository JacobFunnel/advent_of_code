from parse import parse_lines
from collections import defaultdict, namedtuple

hands = {line.split()[0]: int(line.split()[-1]) for line in parse_lines()}
card_ranking = "AKQT98765432J"
card_amount_ranking = [
    [5],  # 5 of a kind
    [4, 1],  # 4 of a kind
    [3, 2],  # full house
    [3, 1, 1],  # 3 of a kind
    [2, 2, 1],  # 2 pair
    [2, 1, 1, 1],  # 1 pair
    [1, 1, 1, 1, 1],  # high card
]


def score_card(card):
    return card_ranking.index(card)


def score_hand(hand):
    card_amounts = defaultdict(int)
    for card in hand:
        if card != "J":
            card_amounts[card] += 1
    n_of_a_kind = sorted(card_amounts.values(), reverse=True)
    if n_of_a_kind in card_amount_ranking:
        return card_amount_ranking.index(n_of_a_kind)
    else:
        return joker_rule_rank(n_of_a_kind)


def joker_rule_rank(n_of_a_kind):
    unique = len(n_of_a_kind)
    for rank, pattern in enumerate(card_amount_ranking):
        if rank == 0 and unique <= len(pattern):
            return rank
        elif unique == len(pattern) and all(n <= p for n, p in zip(n_of_a_kind, pattern)):
            return rank
    return len(card_amount_ranking) - 1


def rank_hands(hands):
    return sorted(
        hands.keys(),
        key=lambda h: (hands[h].hand_score, hands[h].card_scores),
        reverse=True,
    )


hands = {
    hand: namedtuple("hand_values", ["hand_score", "card_scores", "bid"])(
        score_hand(hand), [score_card(c) for c in hand], bid
    )
    for hand, bid in hands.items()
}
sorted_hands = rank_hands(hands)
sorted_bids = [hands[hand].bid for hand in sorted_hands]
print(sum(rank * bid for rank, bid in (zip(range(1, len(sorted_bids) + 1), sorted_bids))))
