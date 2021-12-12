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

ingredients_without_allergens = all_ingredients - ingredients_with_allergens
result = sum(len(ingredients_without_allergens & d[0]) for d in data)
print(result)
