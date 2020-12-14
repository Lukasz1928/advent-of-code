

def read_input():
    with open('input', 'r') as f:
        lines = [line for line in f]
    ts = int(lines[0])
    ids = [int(x) if x.isnumeric() else None for x in lines[1].split(',')]
    return ts, ids


_, buses = read_input()
active_buses = list(sorted([(i, b) for i, b in enumerate(buses) if b is not None], key=lambda x: x[1], reverse=True))
seq = 1, 1
for bus in active_buses:
    elem = 0
    while True:
        v = seq[0] + seq[1] * elem
        if v % bus[1] == (bus[1] - bus[0]) % bus[1]:
            seq = v, seq[1] * bus[1]
            break
        elem += 1
result = seq[0]
print(result)
