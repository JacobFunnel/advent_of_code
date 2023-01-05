with open("input/06.txt", "r") as f:
    groups = f.read().split("\n\n")


def parse(groups):
    groups = [group.split("\n") for group in groups]
    set_groups = []
    for group in groups:
        set_groups.append([set(p) for p in group])
    return set_groups


def count_interserctions(set_groups):
    count = 0
    for set_group in set_groups:
        count += len(set.intersection(*set_group))
    return count


set_groups = parse(groups)
print(count_interserctions(set_groups))
