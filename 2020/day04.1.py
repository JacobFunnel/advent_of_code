import re

with open("input/04.txt", "r") as f:
    lines = f.read().split("\n\n")


def parse(lines):
    entries = []
    for line in lines:
        entry = re.split(" |\n", line)
        entry = {kw[:kw.find(":")] for kw in entry}
        entries.append(entry)
    return entries


def valid(entries):
    req = {"ecl", "pid", "byr", "iyr", "hgt", "hcl", "eyr"}
    count = 0
    for entry in entries:
        if req.issubset(entry):
            count += 1
    return count


print(valid(parse(lines)))
