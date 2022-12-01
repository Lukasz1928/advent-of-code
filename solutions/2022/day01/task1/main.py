def read_input():
    with open('input', 'r') as f:
        groups = f.read().split('\n\n')
    return [tuple(int(line) for line in group.split('\n')) for group in groups]


data = read_input()
result = max(sum(elf) for elf in data)

print(result)
