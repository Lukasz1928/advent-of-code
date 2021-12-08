from functools import reduce


def read_input():
    d = []
    with open('input', 'r') as f:
        for line in f.readlines():
            l, r = line.strip().split('|')
            d.append((tuple(l.split()), tuple(r.split())))
    return d


def get_mapping(d):
    mp = {}
    wires = [set(x) for x in d]
    mp[1] = [x for x in wires if len(x) == 2][0]
    mp[4] = [x for x in wires if len(x) == 4][0]
    mp[7] = [x for x in wires if len(x) == 3][0]
    mp[8] = [x for x in wires if len(x) == 7][0]
    l5 = [x for x in wires if len(x) == 5]
    for i, p in enumerate(l5):
        if all(j == i or p | q in wires for j, q in enumerate(l5)):
            mp[5] = p
    for p in l5:
        if len(mp[5] | p) == 7:
            mp[2] = p
    mp[3] = [x for x in l5 if x != mp[2] and x != mp[5]][0]
    l6 = [x for x in wires if len(x) == 6]
    mp[9] = [x for x in l6 if x & mp[3] == mp[3]][0]
    mp[6] = [x for x in l6 if len(x & mp[1]) == 1][0]
    mp[0] = [x for x in l6 if x != mp[6] and x != mp[9]][0]
    return {tuple(sorted(_v for _v in v)): k for k, v in mp.items()}


def get_value(mapping, digits):
    return reduce(lambda total, current: 10 * total + mapping[tuple(sorted(current))], digits, 0)


data = read_input()
result = sum(get_value(get_mapping(row[0]), row[1]) for row in data)
print(result)
