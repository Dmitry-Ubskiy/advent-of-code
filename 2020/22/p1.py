#!/usr/bin/env python3

decks = []
with open('input') as f:
    for p in f.read().split('\n\n'):
        decks.append(list(map(int, p.strip().split('\n')[1:])))

argmax = lambda a: a.index(max(a))
while all(decks):
    cards = [d.pop(0) for d in decks]
    decks[argmax(cards)].extend(sorted(cards, reverse=True))
score = sum([(i+1) * c for i, c in enumerate(reversed(sum(decks, [])))])
print(score)
