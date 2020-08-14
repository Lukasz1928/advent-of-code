from collections import defaultdict


def parse_instruction(instr):
    ts = instr.split(' ')
    i = (ts[0],)
    i += (ts[1] if ts[1].isalpha() else int(ts[1]), )
    if len(ts) == 3:
        i += (ts[2] if ts[2].isalpha() else int(ts[2]),)
    return i


def read_input():
    with open('input', 'r') as f:
        return [parse_instruction(x.strip()) for x in f]


def value_of(regs, reg):
    if isinstance(reg, int):
        return reg
    return regs[reg]


instrs = read_input()
registers = defaultdict(lambda: 0)
play_frequency = -1
recovered_frequency = -1

i = 0
while True:
    instr = instrs[i]
    if instr[0] == 'snd':
        play_frequency = value_of(registers, instr[1])
        i += 1
    elif instr[0] == 'set':
        registers[instr[1]] = value_of(registers, instr[2])
        i += 1
    elif instr[0] == 'add':
        registers[instr[1]] += value_of(registers, instr[2])
        i += 1
    elif instr[0] == 'mul':
        registers[instr[1]] *= value_of(registers, instr[2])
        i += 1
    elif instr[0] == 'mod':
        registers[instr[1]] %= value_of(registers, instr[2])
        i += 1
    elif instr[0] == 'rcv':
        if value_of(registers, instr[1]) != 0:
            recovered_frequency = play_frequency
            break
        i += 1
    elif instr[0] == 'jgz':
        if value_of(registers, instr[1]) > 0:
            i += value_of(registers, instr[2])
        else:
            i += 1

print(recovered_frequency)
