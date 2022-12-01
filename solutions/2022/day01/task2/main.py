def read_input():
    with open('input', 'r') as f:
        groups = f.read().split('\n\n')
    return [tuple(int(line) for line in group.split('\n')) for group in groups]


data = read_input()
sums = [sum(elf) for elf in data]

maxes = (0, 0, 0)
for s in sums:
    if s > maxes[0]:
        maxes = (s, maxes[0], maxes[1])
    elif s > maxes[1]:
        maxes = (maxes[0], s, maxes[1])
    elif s > maxes[2]:
        maxes = (maxes[0], maxes[1], s)

result = sum(maxes)
print(result)
