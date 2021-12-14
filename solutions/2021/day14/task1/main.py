from collections import Counter


def read_input():
    with open('input', 'r') as f:
        raw_input = f.read()
    l0, prods = raw_input.split('\n\n')
    prod = dict(p.split(' -> ') for p in prods.split('\n'))
    return l0, prod


def step(temp, prods):
    inserts = [prods.get(temp[i:i+2], '') for i in range(len(temp) - 1)]
    return ''.join([e + inserts[i] for i, e in enumerate(temp[:-1])]) + temp[-1]


template, productions = read_input()

for _ in range(10):
    template = step(template, productions)
cnts = Counter(template).most_common()
result = cnts[0][1] - cnts[-1][1]
print(result)
