

def read_input():
    with open('input', 'r') as f:
        return int(f.read().strip())


def new_values(vals, pos):
    s = sum([vals[p] for p in pos])
    return [int(x) for x in [d for d in str(s)]]


recipes_count = read_input()

values = [3, 7]
positions = [0, 1]
while len(values) < recipes_count + 10:
    values_to_add = new_values(values, positions)
    values.extend(values_to_add)
    positions = [(p + 1 + values[p]) % len(values) for p in positions]
selected = values[:recipes_count + 10][-10:]
result = ''.join([str(x) for x in selected])
print(result)
