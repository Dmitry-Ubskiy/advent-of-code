#!/usr/bin/env python3

from collections import defaultdict

occurence = defaultdict(lambda: 0)
allergenic = {}
may_contain = {}
with open('input') as f:
    for line in f:
        ingredients, allergens = line.strip().replace('(', '').replace(')', '').split(' contains ')
        ingredients = set(ingredients.strip().split())
        allergens = set(allergens.strip().replace(',', '').split())
        for i in ingredients:
            occurence[i] += 1
            may_contain.setdefault(i, set())
            may_contain[i] |= allergens
        for a in allergens:
            allergenic.setdefault(a, set(ingredients))
            allergenic[a] &= ingredients

maybe_allergenic = set.union(*list(map(set, allergenic.values())))
defo_allergenic = {}
while allergenic:
    for k in list(allergenic.keys()):
        if len(allergenic[k]) == 1:
            defo_allergenic[k] = next(iter(allergenic[k]))
            del allergenic[k]
    reverse_mapping = {}
    for k, vs in allergenic.items():
        for v in vs:
            reverse_mapping.setdefault(v, set())
            reverse_mapping[v].add(k)
    for v in list(reverse_mapping.keys()):
        if len(reverse_mapping[v]) == 1:
            k = next(iter(reverse_mapping[v]))
            defo_allergenic[k] = v
            del allergenic[k]
print(','.join([defo_allergenic[k] for k in sorted(defo_allergenic.keys())]))
