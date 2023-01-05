with open("input/03.txt", "r") as f:
    rucksacks = [{*sack} for sack in f.read().splitlines()]

badges, priorities = [], []

for i in range(0, len(rucksacks), 3):
    badges.append(list(set.intersection(*rucksacks[i:i + 3]))[0])

for badge in badges:
    priority = ord(badge)
    if badge.isupper():
        priority -= 38
    else:
        priority -= 96
    priorities.append(priority)

print(sum(priorities))
