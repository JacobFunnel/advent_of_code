with open("../input/day14_input.txt", "r") as f:
    in_put = [line.strip() for line in f.readlines()]

template = in_put[0]
ins_dict = {}

for line in in_put[2:]:
    a, b = line.split(" -> ")
    ins_dict.update({a: b})

for step in range(1):
    print(step)
    for i in range(-len(template), -1):
        first = template[: i + 1]
        key = template[i : i + 2]
        value = ins_dict[template[i : i + 2 or None]]
        end = template[i + 1 :]
        template = template[: i + 1] + ins_dict[template[i : i + 2 or None]] + template[i + 1 :]

keys = set(template)
occurences = sorted([template.count(key) for key in keys])
print(occurences[-1] - occurences[0])

sum = 2
for i in range(40):
    sum += sum - 1
print(sum)
