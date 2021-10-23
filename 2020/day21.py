inputs_ = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''


def structure(inputs):
    # calculate for each allergen get possible ingredients
    # gather all ingredients
    allergens_to_ingredients = {}
    all_ingredients = set()
    for line in inputs.splitlines():
        ingredients, allergens = line[:-1].split(' (contains ')
        ingredients = ingredients.split()
        allergens = allergens.split(', ')
        all_ingredients |= set(ingredients)
        for a in allergens:
            if a not in allergens_to_ingredients:
                allergens_to_ingredients[a] = set(ingredients)
            else:
                allergens_to_ingredients[a] &= set(ingredients)

    # remove from all ingredients any which are possible allergens
    safe_ingredients = all_ingredients
    for ingredients in allergens_to_ingredients.values():
        for ing in ingredients:
            if ing in safe_ingredients:
                safe_ingredients.remove(ing)

    return allergens_to_ingredients, safe_ingredients


def first(safe_ingredients):
    count = 0
    for line in inputs_.splitlines():
        ings, alls = line[:-1].split(' (contains ')
        ings = set(ings.split())

        count += len(ings & safe_ingredients)
    return count


def second(allergens_to_ings):
    dictionary = {}
    while len(dictionary) < len(allergens_to_ings):
        for allerg, ing in allergens_to_ings.items():
            if len(ing) == 1:
                dictionary[allerg] = list(ing)[0]
            else:
                allergens_to_ings[allerg] = list(
                    set(ing) - set(dictionary.values())
                )

    allergens = sorted(dictionary.keys())
    return ','.join(dictionary[a] for a in allergens)


if __name__ == '__main__':
    with open('src/day21.txt') as fp:
        inputs_ = fp.read()
    a_to_i, safe_i = structure(inputs_)
    print(first(safe_i))
    print(second(a_to_i))
