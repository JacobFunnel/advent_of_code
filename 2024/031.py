import re

from parse import parse_lines

memory = "".join(parse_lines())
mul_a_b_pattern = r"mul\(\d+,\d+\)"
total = 0
for match_ in re.findall(mul_a_b_pattern, memory):
    a, b = re.findall(r"\d+", match_)
    total += int(a) * int(b)

print(total)
