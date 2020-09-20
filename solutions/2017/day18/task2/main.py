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


class Computer:
    def __init__(self, instructions, pvalue):
        self.instrs = instructions
        self.registers = defaultdict(lambda: 0)
        self.registers['p'] = pvalue
        self.ip = 0
        self.input_buffer = []
        self.other_computer = None
        self.values_sent = 0

    def can_be_run(self):
        return self.instrs[self.ip][0] != 'rcv' or len(self.input_buffer) > 0

    def run(self):
        instr = self.instrs[self.ip]
        if instr[0] == 'snd':
            self.other_computer.input_buffer.append(value_of(self.registers, instr[1]))
            self.values_sent += 1
            self.ip += 1
            return 0
        elif instr[0] == 'set':
            self.registers[instr[1]] = value_of(self.registers, instr[2])
            self.ip += 1
            return 0
        elif instr[0] == 'add':
            self.registers[instr[1]] += value_of(self.registers, instr[2])
            self.ip += 1
            return 0
        elif instr[0] == 'mul':
            self.registers[instr[1]] *= value_of(self.registers, instr[2])
            self.ip += 1
            return 0
        elif instr[0] == 'mod':
            self.registers[instr[1]] %= value_of(self.registers, instr[2])
            self.ip += 1
            return 0
        elif instr[0] == 'rcv':
            if len(self.input_buffer) > 0:
                self.registers[instr[1]] = self.input_buffer.pop(0)
                self.ip += 1
                return 0
            else:
                return 1
        elif instr[0] == 'jgz':
            if value_of(self.registers, instr[1]) > 0:
                self.ip += value_of(self.registers, instr[2])
            else:
                self.ip += 1


instrs = read_input()
c1 = Computer(instrs, 0)
c2 = Computer(instrs, 1)

c1.other_computer = c2
c2.other_computer = c1

while c1.can_be_run() or c2.can_be_run():
    r = 0
    while r == 0:
        r = c1.run()
    r = 0
    while r == 0:
        r = c2.run()

result = c2.values_sent
print(result)
