from parse import parse_lines


def lavahash(seq):
    value = 0
    for char in seq:
        value = (value + ord(char)) * 17 % 256
    return value


seqs = parse_lines()[0].split(",")
print(sum(lavahash(seq) for seq in seqs))
