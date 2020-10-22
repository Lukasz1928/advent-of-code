

def read_input():
    with open('input', 'r') as f:
        return f.read().strip()


value_to_find = read_input()

values = '37'
positions = [0, 1]
while value_to_find not in values[-(len(value_to_find) + 2):]:
    values += str(sum([int(values[p]) for p in positions]))
    positions = [(p + 1 + int(values[p])) % len(values) for p in positions]

result = values.index(value_to_find)
print(result)
