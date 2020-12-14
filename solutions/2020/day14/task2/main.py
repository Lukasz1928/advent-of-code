import re
from collections import defaultdict


def read_input():
    with open('input', 'r') as f:
        return [line for line in f]


def apply_mask(value, mask):
    val = bin(value)[2:].zfill(36)
    values = ['']
    for b, m in list(zip(val, mask)):
        if m == '0':
            values = [v + b for v in values]
        elif m == '1':
            values = [v + '1' for v in values]
        else:
            values = [v + '0' for v in values] + [v + '1' for v in values]
    return [int(x, 2) for x in values]


program = read_input()
memory = defaultdict(lambda: 0)
mask = None
for instr in program:
    if instr.startswith('mask'):
        mask = instr[7:]
    else:
        m = re.match(r'mem\[(\d+)\] = (\d+)', instr)
        v = int(m.group(2))
        for addr in apply_mask(int(m.group(1)), mask):
            memory[addr] = v
result = sum(memory.values())
print(result)
