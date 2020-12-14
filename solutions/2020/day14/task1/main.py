import re
from collections import defaultdict


def read_input():
    with open('input', 'r') as f:
        return [line for line in f]


def apply_mask(value, mask):
    val = bin(value)[2:].zfill(36)
    ditgits = [d if mask[i] == 'X' else mask[i] for i, d in enumerate(val)]
    return int(''.join(ditgits), 2)


program = read_input()
memory = defaultdict(lambda: 0)
mask = None
for instr in program:
    if instr.startswith('mask'):
        mask = instr[7:]
    else:
        m = re.match(r'mem\[(\d+)\] = (\d+)', instr)
        memory[int(m.group(1))] = apply_mask(int(m.group(2)), mask)
result = sum(memory.values())
print(result)
