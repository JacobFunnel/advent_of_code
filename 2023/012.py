from parse import parse_lines

signals = parse_lines()
total = 0
references = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

for signal in signals:
    values = [
        value
        for index, _ in enumerate(signal)
        for ref, value in references.items()
        if signal.startswith(ref, index)
    ]
    total += int(values[0] + values[-1])

print(total)
