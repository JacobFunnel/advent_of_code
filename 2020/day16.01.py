import re

with open("input/16.txt", "r") as f:
    raw_rules, my_raw_ticket, raw_nearby_tickets = f.read().split("\n\n")

rules = {row[:row.find(":")]: list(map(int, re.split(" or |-", row[row.find(":") + 2:])))
         for row in raw_rules.split("\n")}
my_ticket = [int(x) for x in my_raw_ticket[my_raw_ticket.find("\n") + 1:].split(",")]
nearby_tickets = [list(map(int, row.split(",")))
                  for row in raw_nearby_tickets[raw_nearby_tickets.find("\n") + 1:].split("\n")]


def create_range_set(params):
    a, b, c, d = params
    return set(range(a, b + 1)) | set(range(c, d + 1))


for rule, value_list in rules.items():
    rules[rule] = create_range_set(value_list)

all_valid = set().union(*rules.values())
all_invalid = []
for ticket in nearby_tickets:
    for value in ticket:
        if not {value}.issubset(all_valid):
            all_invalid.append(value)

print(sum(all_valid))

all_nearby_values = set().union(*nearby_tickets)
print(sum(all_nearby_values.intersection(all_valid)))
