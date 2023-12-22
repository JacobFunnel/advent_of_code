with open("input/07.txt", "r") as f:
    lines = f.read().split("\n")


def parse(lines):
    rules = {}
    for line in lines:
        bag, contents = line.split(" bags contain ")
        contents = contents.split(", ")
        sub_rules = {}
        for content in contents:
            sub_rules.update(parse_content(content))
        rules.update({bag: sub_rules})
    return rules


def parse_content(content):
    try:
        amount = int(content[: content.find(" ")])
    except ValueError:
        return {}
    bag = content[content.find(" ") + 1 : content.find(" bag")]
    return {bag: amount}


def delve_from_bag_to_bag(from_bag, to_bag, rules):
    if from_bag == to_bag:
        return False
    elif to_bag in rules[from_bag]:
        return True
    else:
        for bag in rules[from_bag]:
            if delve_from_bag_to_bag(bag, to_bag, rules):
                return True
        return False


rules = parse(lines)
count = 0
for bag in rules.keys():
    if delve_from_bag_to_bag(bag, "shiny gold", rules):
        count += 1

print(count)
