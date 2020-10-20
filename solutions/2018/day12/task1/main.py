

def read_input():
    with open('input', 'r') as f:
        lines = [l.strip().replace(' ', '') for l in f]
    ini = lines[0].split(':')[1]
    rules = []
    for r in lines[2:]:
        l, r = r.split('=>')
        rules.append((l, r))
    return rules, ini


def fill(state):
    i = 0
    while state[i] == '.' and i < 5:
        i += 1
    j = 0
    while state[-j] == '.' and j < 5:
        j += 1
    return (5 - i), '.' * (5 - i) + state + '.' * (5 - j)


def transform(state, transformations):
    added, filled_state = fill(state)
    new_state = ''
    for i in range(2, len(filled_state) - 2):
        part = filled_state[i - 2:i + 3]
        for t in transformations:
            if t[0] == part:
                new_state += t[1]
                break
    transformed = filled_state[:2] + new_state + filled_state[-2:]
    return added, transformed


rules, state = read_input()
left_index = 0
for _ in range(20):
    a, state = transform(state, rules)
    left_index -= a

numbers_sum = 0
for i, p in enumerate(state):
    if p == '#':
        numbers_sum += i + left_index
print(numbers_sum)
