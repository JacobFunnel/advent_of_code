with open("input/21.txt", "r") as f:
    lines = f.readlines()

i_a_tuples = [
    (
        set(line[: line.find(" (")].split()),
        set(line[line.find("(") + 10 : line.find(")")].split(", ")),
    )
    for line in lines
]
# ingredients to allergens mapping

all_allergens = set().union(*[allergens for ingredients, allergens in i_a_tuples])

a_to_i = {}
#  allergens to ingredients mapping
for allergen in all_allergens:
    possible_ingredients = [
        ingredients for ingredients, allergens in i_a_tuples if allergen in allergens
    ]
    a_to_i[allergen] = set.intersection(*possible_ingredients)

identified_a_to_i = {}
while len(identified_a_to_i.keys()) != len(a_to_i.keys()):
    for allergen, ingredients in a_to_i.items():
        if len(ingredients) == 1 and allergen not in identified_a_to_i.keys():
            identified_a_to_i[allergen] = list(ingredients)[0]
    for ingredient in identified_a_to_i.values():
        for ingredients in a_to_i.values():
            ingredients.discard(ingredient)

print(",".join(dict(sorted(identified_a_to_i.items(), key=lambda item: item[0])).values()))
