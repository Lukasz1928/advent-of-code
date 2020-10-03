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
    def __init__(self, instructions):
        self.instrs = instructions
        self.registers = None
        self.reset()
        self.ip = 0

    def reg_values(self):
        return self.registers['a'], self.registers['b'], self.registers['c'], self.registers['d']

    def reset(self):
        self.registers = defaultdict(lambda: 0)
        self.registers['c'] = 1
        self.ip = 0

    def can_be_run(self):
        return 0 <= self.ip < len(self.instrs)

    def run_to_end(self):
        while self.can_be_run():
            self.run()

    def run(self):
        # print(self.ip, dict(self.registers))
        instr = self.instrs[self.ip]
        if instr[0] == 'cpy':
            if isinstance(instr[2], int):
                return None
            self.registers[instr[2]] = value_of(self.registers, instr[1])
            self.ip += 1
            return None
        elif instr[0] == 'inc':
            if isinstance(instr[1], int):
                return None
            self.registers[instr[1]] += 1
            self.ip += 1
            return None
        elif instr[0] == 'dec':
            if isinstance(instr[1], int):
                return None
            self.registers[instr[1]] -= 1
            self.ip += 1
            return None
        elif instr[0] == 'jnz':
            if value_of(self.registers, instr[1]) != 0:
                self.ip += value_of(self.registers, instr[2])
            else:
                self.ip += 1
            return None
        elif instr[0] == 'out':
            value = value_of(self.registers, instr[1])
            self.ip += 1
            return value


def is_periodic(comp, initial_value):
    comp.reset()
    comp.registers['a'] = initial_value
    steps_limit = 10000
    reg_values0 = set()
    reg_values1 = set()
    prev = 1
    for step in range(steps_limit):
        if not comp.can_be_run():
            return False
        r = None
        cnt = 0
        while r is None:
            r = comp.run()
            cnt += 1
            if cnt == 25000:
                return False
        regs = comp.reg_values()
        if r == 0:
            if prev != 1:
                return False
            if regs in reg_values0:
                return True
            reg_values0.add(regs)
        elif r == 1:
            if prev != 0:
                return False
            if regs in reg_values1:
                return True
            reg_values1.add(regs)
        else:
            return False
        prev = r
    return True


instrs = read_input()
c = Computer(instrs)
initial_value = 1
while True:
    if is_periodic(c, initial_value):
        break
    initial_value += 1
result = initial_value
print(result)
