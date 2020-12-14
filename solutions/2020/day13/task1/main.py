

def read_input():
    with open('input', 'r') as f:
        lines = [line for line in f]
    ts = int(lines[0])
    ids = [int(x) if x.isnumeric() else None for x in lines[1].split(',')]
    return ts, ids


earliest_time, buses = read_input()
active_buses = [b for b in buses if b is not None]
timestamp = earliest_time
bus = None
while bus is None:
    for b in [x for x in active_buses]:
        if timestamp % b == 0:
            bus = b
            break
    timestamp += 1

result = bus * (timestamp - 1 - earliest_time)
print(result)
