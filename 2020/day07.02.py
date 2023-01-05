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
        amount = int(content[:content.find(" ")])
    except ValueError:
        return {}
    bag = content[content.find(" ") + 1:content.find(" bag")]
    return {bag: amount}


def count_inner_bags(from_bag, rules):
    if not rules[from_bag]:
        return 0
    else:
        count = 0
        for bag, amount in rules[from_bag].items():
            count += amount + amount * count_inner_bags(bag, rules)
        return count


rules = parse(lines)
print(count_inner_bags("shiny gold", rules))
