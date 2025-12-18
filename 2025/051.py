from parse import parse_lines

ranges, ids = parse_lines(2)
ranges = [tuple(map(int, r.split("-"))) for r in ranges.splitlines()]
ids = [int(id_) for id_ in ids.splitlines()]


def is_in_range(point, range_):
    return point >= range_[0] and point <= range_[1]


def is_in_any_range(point, ranges):
    return any(is_in_range(point, range_) for range_ in ranges)


print(sum(1 for id_ in ids if is_in_any_range(id_, ranges)))
