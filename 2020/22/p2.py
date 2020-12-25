#!/usr/bin/env python3

decks = []
with open('input') as f:
    for p in f.read().split('\n\n'):
        decks.append(list(map(int, p.strip().split('\n')[1:])))

argmax = lambda a: a.index(max(a))

def recursive_combat(decks):
    prev_rounds = set()

    while all(decks):
        round_hash = repr(decks)  # lol
        if round_hash in prev_rounds:
            return 0, None
        prev_rounds.add(round_hash)

        cards = [d.pop(0) for d in decks]

        if all(len(decks[i]) >= c for i, c in enumerate(cards)):
            winner, _ = recursive_combat([d[:c] for d, c in zip(decks, cards)])
            cards = [c for i, c in sorted(enumerate(cards), key=lambda a: a[0] == winner, reverse=True)]
        else:
            winner = argmax(cards)
            cards.sort(reverse=True)

        decks[winner].extend(cards)
    winner = argmax(list(map(len, decks)))
    score = sum([(i+1) * c for i, c in enumerate(reversed(decks[winner]))])
    return winner, score

print(recursive_combat(decks)[1])
