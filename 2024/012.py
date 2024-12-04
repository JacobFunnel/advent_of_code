from parse import parse_lines

ll, rl = [], []
for left, right in (line.split("   ") for line in parse_lines() if line):
    ll.append(int(left))
    rl.append(int(right))

rl_count = {value: rl.count(value) for value in set(rl)}
similarity = sum(rl_count.get(value, 0) * value for value in ll)
print(similarity)
