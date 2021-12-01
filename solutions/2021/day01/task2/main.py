
def read_input():
    with open('input', 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


depths = read_input()
sums = [sum(depths[s:s+3]) for s in range(0, len(depths) - 2)]
result = sum([d > sums[i - 1] for i, d in enumerate(sums[1:], 1)])
print(result)
