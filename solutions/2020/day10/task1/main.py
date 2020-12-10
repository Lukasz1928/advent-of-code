
def read_input():
    with open('input', 'r') as f:
        return [int(line.strip()) for line in f]


voltages = read_input()
sorted_voltages = list(sorted(voltages))
sorted_voltages += [sorted_voltages[-1] + 3]

prev = 0
difs = [0, 0, 0]
for voltage in sorted_voltages:
    dv = voltage - prev
    difs[dv - 1] += 1
    prev = voltage
result = difs[0] * difs[2]
print(result)
