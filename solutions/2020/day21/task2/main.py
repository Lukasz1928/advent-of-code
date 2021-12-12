from functools import reduce


def read_input():
    ret = []
    with open('input', 'r') as f:
        for line in f.readlines():
            l, r = line.strip().split('(')
            ingredients = set(l[:-1].split(' '))
            allergens = set(r[9:-1].split(', '))
            ret.append((ingredients, allergens))
    return ret


data = read_input()
all_allergens = reduce(lambda agg, curr: agg | curr[1], data, set())
all_ingredients = reduce(lambda agg, curr: agg | curr[0], data, set())

allergen_in = {allergen: reduce(lambda agg, curr: agg & curr[0] if allergen in curr[1] else agg, data, all_ingredients)
               for allergen in all_allergens}
ingredients_with_allergens = reduce(lambda agg, curr: agg | curr, allergen_in.values(), set())
data = [(x & ingredients_with_allergens, y) for (x, y) in data]


allergen_possible_ingredients = {allergen: [p[0] for p in data if allergen in p[1]] for allergen in all_allergens}
allergen_ingredient = {}
while allergen_possible_ingredients:
    for allergen, ings in allergen_possible_ingredients.items():
        intersection = reduce(lambda agg, curr: agg & curr, ings, ings[0])
        if len(intersection) == 1:
            ingredient = intersection.pop()
            allergen_ingredient[ingredient] = allergen
            del allergen_possible_ingredients[allergen]
            break
    allergen_possible_ingredients = {k: [s - {ingredient} for s in v] for k, v in allergen_possible_ingredients.items()}
ordered_ingredients = list(sorted(allergen_ingredient.items(), key=lambda x: x[1]))
result = ','.join([k for (k, v) in ordered_ingredients])
print(result)
