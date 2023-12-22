import re
from itertools import product

from parse import parse_lines


def parse():
    springs = []
    for raw, groups in (line.split() for line in parse_lines()):
        seqs = list(re.findall(r"[^.]+", raw))
        groups = [int(n) for n in groups.split(",")]
        springs.append([raw, seqs, [len(seq) for seq in seqs], groups])
    return springs


def compare_and_reduce_group_sizes(seqs, seq_ls, groups):
    if len(seq_ls) == len(groups):
        return seqs, seq_ls, groups
    else:
        while seq_ls[0] == groups[0]:
            seqs.pop(0)
            seq_ls.pop(0)
            groups.pop(0)
        while seq_ls[-1] == groups[-1]:
            seqs.pop(-1)
            seq_ls.pop(-1)
            groups.pop(-1)
        return seqs, seq_ls, groups


def find_arrangements(seqs, seq_ls, groups):
    print(seqs, seq_ls, groups)


def find_valid_chunks(seqs, seq_ls, groups):
    # loops indefinitely for:
    # #???..#.?#??# ['#???', '#', '?#??#'] [4, 1, 5] [2, 1, 2, 1]
    # need to check for hard limits before chunking, or chunk even smarter
    if len(seq_ls) == len(groups):
        return (([obj] for obj in tup) for tup in zip(seqs, seq_ls, groups))
    else:
        chunks = []
        while groups:
            subgroups = []
            while True:
                if sum(subgroups) + groups[0] <= seq_ls[0]:
                    subgroups.append(groups.pop(0))
                    if not groups:
                        break
                else:
                    break
            if subgroups:
                chunks.append(([seqs.pop(0)], [seq_ls.pop(0)], subgroups))
            else:
                chunks.append((seqs, seq_ls, groups))
        return chunks


springs = parse()
for raw, seqs, seq_ls, groups in springs:
    print(raw, seqs, seq_ls, groups)
    seqs, seq_ls, groups = compare_and_reduce_group_sizes(seqs, seq_ls, groups)
    chunks = find_valid_chunks(seqs, seq_ls, groups)
    for chunk in chunks:
        find_arrangements(*chunk)


def brute(raw, groups):
    indices = [idx for idx, char in enumerate(raw) if char == "?"]
    combinations = product(".#", repeat=len(indices))
    ways = 0
    for combo in combinations:
        combo = (n for n in combo)
        new_seq = "".join(
            char if idx not in indices else next(combo) for idx, char in enumerate(raw)
        )
        new_groups = [len(group) for group in (re.findall(r"#+", new_seq))]
        if new_groups == groups:
            ways += 1
    return ways
