with open("input/03.txt", "r") as f:
    rucksacks = [(sack[:int(len(sack)/2)], sack[int(len(sack)/2):])
                 for sack in f.read().splitlines()]

item_types = [list({*sack[0]}.intersection({*sack[-1]}))[0] for sack in rucksacks]
priorities = []
for item_type in item_types:
    priority = ord(item_type)
    if item_type.isupper():
        priority -= 38
    else:
        priority -= 96
    priorities.append(priority)

print(sum(priorities))
