with open('../input/day08_input.txt', 'r') as f:
    codes = [[b.split() for b in a.split('|')] for a in f.readlines()]

segments = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
occurrences = {value: list(segments.values()).count(value) for value in sorted(list(set(segments.values())))}
unique = {i for i in occurrences if occurrences[i] == 1}

count = 0
for pair in codes:
    _, output = pair
    for element in output:
        if len(element) in unique:
            count += 1

print(count)