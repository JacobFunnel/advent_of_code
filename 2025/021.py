from parse import parse_all

pairs = (tuple(map(int, block.split("-"))) for block in parse_all().split(","))
total = 0
for s, e in pairs:
    for n in range(s, e + 1):
        s = str(n)
        l = len(s)
        if l % 2 == 0 and s[: l // 2] == s[l // 2 :]:
            total += n

print(total)
