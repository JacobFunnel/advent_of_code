from parse import parse_lines

banks = [list(map(int, line)) for line in parse_lines()]
total = 0
for bank in banks:
    digit1 = max(bank[:-1])
    digit2 = max(bank[bank.index(digit1) + 1 :])
    total += digit1 * 10 + digit2
print(total)
