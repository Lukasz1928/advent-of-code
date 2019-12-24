import regex

lines = open('input', 'r').read().splitlines()


def deal_into_new_stack(cards):
    return list(reversed(cards))


def cut(cards, N):
    return cards[N:] + cards[:N]


def deal_with_increment(cards, inc):
    l = len(cards)
    d = [None] * l
    index = 0
    for c in cards:
        d[index] = c
        index = (index + inc) % l
    return d


def apply(cards, op):
    if op == 'deal into new stack':
        return deal_into_new_stack(cards)
    r = regex.match(r'cut (-?\d+)', op)
    if r is not None:
        return cut(cards, int(r[1]))
    r = regex.match(r'deal with increment (\d+)', op)
    if r is not None:
        return deal_with_increment(cards, int(r[1]))


cards = list(range(10007))
for op in lines:
    cards = apply(cards, op)
print(cards.index(2019))
