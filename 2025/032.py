from parse import parse_lines

banks = [list(map(int, line)) for line in parse_lines()]


def joltage(bank):
    digits = []
    current_index = -1
    for n in range(11, -1, -1):
        digit = max(bank[current_index + 1 : -n or None])
        current_index = bank.index(digit, current_index + 1)
        digits.append(digit)
    return int("".join(map(str, digits)))


print(sum(joltage(bank) for bank in banks))
