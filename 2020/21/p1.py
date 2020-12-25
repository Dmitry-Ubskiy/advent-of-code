#!/usr/bin/env python3

from collections import defaultdict

occurence = defaultdict(lambda: 0)
allergenic = {}
with open('input') as f:
    for line in f:
        ingredients, allergens = line.strip().replace('(', '').replace(')', '').split(' contains ')
        ingredients = set(ingredients.strip().split())
        allergens = allergens.strip().replace(',', '').split()
        for i in ingredients:
            occurence[i] += 1
        for a in allergens:
            allergenic.setdefault(a, ingredients)
            allergenic[a] &= ingredients

maybe_allergenic = set.union(*list(map(set, allergenic.values())))
print(sum(n for i, n in occurence.items() if i not in maybe_allergenic))
