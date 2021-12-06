from collections import Counter


def read_input():
    with open('input', 'r') as f:
        return [int(x) for x in f.read().split(',')]


def step(d):
    new = d[0]
    for k in range(8):
        d[k] = d[k + 1]
    d[8] = new
    d[6] += new
    return d


raw_input = read_input()
initial_days = dict(Counter(raw_input))
days = {key: initial_days.get(key, 0) for key in range(9)}

for _ in range(256):
    days = step(days)
result = sum(days.values())
print(result)
