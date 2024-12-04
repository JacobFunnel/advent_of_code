from parse import parse_lines

ll, rl = [], []
for left, right in (line.split("   ") for line in parse_lines() if line):
    ll.append(int(left))
    rl.append(int(right))

ll, rl = sorted(ll), sorted(rl)
differences = (abs(l - r) for l, r in zip(ll, rl))
print(sum(differences))
