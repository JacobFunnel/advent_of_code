from parse import parse_lines


def next_number(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ (n // 32)) % 16777216
    return (n ^ (n * 2048)) % 16777216

numbers = [int(line) for line in parse_lines() if line]
for _ in range(2000):
    numbers = [next_number(number) for number in numbers]

print(sum(numbers))
