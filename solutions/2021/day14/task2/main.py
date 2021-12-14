from collections import Counter, defaultdict


def read_input():
    with open('input', 'r') as f:
        raw_input = f.read()
    l0, prods = raw_input.split('\n\n')
    prod = dict(p.split(' -> ') for p in prods.split('\n'))
    return l0, prod


def step(cnts, prods):
    new_cnts = defaultdict(lambda: 0, cnts)
    for pair, count in cnts.items():
        if pair in prods:
            new_cnts[pair] = max(new_cnts[pair] - count, 0)
            new_symbol = prods[pair]
            new_cnts[pair[0] + new_symbol] += count
            new_cnts[new_symbol + pair[1]] += count
    return {k: v for k, v in new_cnts.items() if v > 0}


def count_letters(counts, initial_template):
    cnts = defaultdict(lambda: 0)
    for k, v in counts.items():
        cnts[k[0]] += v
        cnts[k[1]] += v
    cnts[initial_template[0]] += 1
    cnts[initial_template[-1]] += 1
    return {k: v // 2 for k, v in cnts.items()}


template, productions = read_input()
counts = dict(Counter([template[i:i+2] for i in range(len(template) - 1)]))
for _ in range(40):
    counts = step(counts, productions)
letter_count = count_letters(counts, template)
result = max(letter_count.values()) - min(letter_count.values())
print(result)
