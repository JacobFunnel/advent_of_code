import re
from fractions import Fraction
from math import ceil

with open("input/14.txt", "r") as f:
    lines = [
        [pair for pair in zip(re.findall(r"[A-Z]+", line), map(int, re.findall(r"\d+", line)))]
        for line in f.readlines()
    ]

o_from_i = {line[-1][0]: (line[-1][1], line[:-1]) for line in lines}
ore_spent = 0
inventory = {k: 0 for k in o_from_i.keys()}


def get_recipy(element_needed, amount_needed):
    global inventory, ore_spent

    amount_produced, ingredients = o_from_i[element_needed]
    multiple = ceil(amount_needed / amount_produced)

    for ingredient, amount in ingredients:
        if ingredient == "ORE":
            ore_spent += amount * multiple
            inventory[element_needed] += amount_produced * multiple
            return [(None, 0)]
        else:
            add_amount_needed = amount - inventory[ingredient]
            if add_amount_needed <= 0:
                inventory[ingredient] -= amount
            else:
                get_recipy(ingredient, amount * multiple)


print(get_recipy("VMBM", 3))
print("hello")
