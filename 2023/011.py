from parse import parse_lines

signals = parse_lines()
total = 0

for signal in signals:
    value = ""
    for char in signal:
        if char.isdigit():
            value += char
    total += int(value[0] + value[-1])

print(total)
