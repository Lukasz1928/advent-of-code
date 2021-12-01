
def read_input():
    with open('input', 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


depths = read_input()
result = sum([d > depths[i - 1] for i, d in enumerate(depths[1:], 1)])
print(result)
