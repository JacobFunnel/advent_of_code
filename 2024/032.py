import re

from itertools import batched
from parse import parse_lines

memory = "".join(parse_lines())
do_s = [match_.end(0) for match_ in re.finditer(r"do\(\)", memory)]
dont_s = [match_.end(0) for match_ in re.finditer(r"don't\(\)", memory)]
all_indices = sorted(do_s + dont_s)
relevant_indices = [0]
do = True
for idx in all_indices:
    if do and idx in dont_s:
        relevant_indices.append(idx)
        do = False
    if not do and idx in do_s:
        relevant_indices.append(idx)
        do = True

total = 0
mul_a_b_pattern = r"mul\(\d+,\d+\)"
for do, dont in batched(relevant_indices, 2):
    for match_ in re.findall(mul_a_b_pattern, memory[do:dont]):
        a, b = re.findall(r"\d+", match_)
        total += int(a) * int(b)

print(total)
