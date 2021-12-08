
def read_input():
    d = []
    with open('input', 'r') as f:
        for line in f.readlines():
            l, r = line.strip().split('|')
            d.append((tuple(l.split()), tuple(r.split())))
    return d


data = read_input()
result = sum(len([x for x in d[1] if len(x) in {2, 3, 4, 7}]) for d in data)
print(result)
