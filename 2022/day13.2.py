with open("input/13.txt", "r") as f:
    packs = [eval(entry) for pair in f.read().split("\n\n") for entry in pair.splitlines()]

div_packs = [[[2]], [[6]]]
packs.extend(div_packs)
pack_by_idx = {i: v for i, v in enumerate(packs)}


def in_order(left, right):
    match left, right:
        case int(), int():
            return True if left < right else None if left == right else False
        case list(), list():
            for i in range(len(left)):
                try:
                    result = in_order(left[i], right[i])
                    if result is not None:
                        return result
                    else:
                        continue
                except IndexError:
                    return False
            if len(left) == len(right):
                return None
            else:
                return True
        case int(), list():
            return in_order([left], right)
        case list(), int():
            return in_order(left, [right])


def get_decoder_key(pack_by_idx):
    score_matrix = [[None for x in range(len(pack_by_idx))] for y in range(len(pack_by_idx))]
    target_indices = list(pack_by_idx.keys())[-2:]
    for l_idx, left in pack_by_idx.items():
        for r_idx, right in pack_by_idx.items():
            if r_idx != l_idx and score_matrix[l_idx][r_idx] is None:
                score_matrix[l_idx][r_idx] = int(in_order(left, right))
                score_matrix[r_idx][l_idx] = int(not (score_matrix[l_idx][r_idx]))

    for i in range(len(score_matrix)):
        score_matrix[i][i] = 0

    order_sums = {i: sum(row) for i, row in enumerate(score_matrix)}
    order_sums = sorted(order_sums.items(), key=lambda item: item[1], reverse=True)
    sorted_indices = [
        sorted_idx + 1 for sorted_idx, (idx, _) in enumerate(order_sums) if idx in target_indices
    ]
    return sorted_indices[0] * sorted_indices[-1]


print(get_decoder_key(pack_by_idx))
