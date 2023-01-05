with open("input/06.txt", "r") as f:
    groups = f.read().split("\n\n")


def parse_and_count(groups):
    counts = [len(set(group) - {"\n"}) for group in groups]
    return sum(counts)


print(parse_and_count(groups))
