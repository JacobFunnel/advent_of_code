import re

with open("input/04.txt", "r") as f:
    lines = f.read().split("\n\n")


def parse(lines):
    entries = []
    for line in lines:
        entry = re.split(" |\n", line)
        entry = {pair[:pair.find(":")]: pair[pair.find(":") + 1:] for pair in entry}
        entries.append(entry)
    return entries


def validate(entries):
    count = 0
    for entry in entries:
        count += check(entry)
    return count


def check(entry):
    req = {"ecl", "pid", "byr", "iyr", "hgt", "hcl", "eyr"}
    if not req.issubset(set(entry.keys())):
        return 0
    if not 1920 <= int(entry["byr"]) <= 2002 or len(entry["byr"]) != 4:
        return 0
    if not 2010 <= int(entry["iyr"]) <= 2020 or len(entry["iyr"]) != 4:
        return 0
    if not 2020 <= int(entry["eyr"]) <= 2030 or len(entry["eyr"]) != 4:
        return 0
    try:
        unit = entry["hgt"][-2:]
        height = entry["hgt"][:-2]
        if (unit == "in" and len(height) != 2) or (unit == "cm" and len(height) != 3):
            return 0
        height = int(height)
        if unit == "in" and not 59 <= height <= 76 or unit == "cm" and not 150 <= height <= 193:
            return 0
    except ValueError:
        return 0
    if re.fullmatch("#([a-f]|[0-9]){6}", entry["hcl"]) is None:
        return 0
    if entry["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return 0
    if re.fullmatch("[0-9]{9}", entry["pid"]) is None:
        return 0
    return 1


print(validate(parse(lines)))
