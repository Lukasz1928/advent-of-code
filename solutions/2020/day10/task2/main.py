

def read_input():
    with open('input', 'r') as f:
        return [int(line.strip()) for line in f]


raw_voltages = read_input()
sorted_voltages = list(sorted(raw_voltages))
voltages = [0] + sorted_voltages + [sorted_voltages[-1] + 3]

paths = [1]
for i, v in enumerate(voltages[1:], 1):
    paths.append(sum([p for idx, p in enumerate(paths) if voltages[idx] >= v - 3]))
result = paths[-1]
print(result)
