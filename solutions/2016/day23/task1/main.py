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
        self.registers = defaultdict(lambda: 0)
        self.registers['c'] = 1
        self.ip = 0

    def can_be_run(self):
        return 0 <= self.ip < len(self.instrs)

    def run_to_end(self):
        while self.can_be_run():
            self.run()

    def run(self):
        instr = self.instrs[self.ip]
        if instr[0] == 'cpy':
            if isinstance(instr[2], int):
                return 0
            self.registers[instr[2]] = value_of(self.registers, instr[1])
            self.ip += 1
            return 0
        elif instr[0] == 'inc':
            if isinstance(instr[1], int):
                return 0
            self.registers[instr[1]] += 1
            self.ip += 1
            return 0
        elif instr[0] == 'dec':
            if isinstance(instr[1], int):
                return 0
            self.registers[instr[1]] -= 1
            self.ip += 1
            return 0
        elif instr[0] == 'jnz':
            if value_of(self.registers, instr[1]) != 0:
                self.ip += value_of(self.registers, instr[2])
            else:
                self.ip += 1
            return 0
        elif instr[0] == 'tgl':
            addr = self.ip + value_of(self.registers, instr[1])
            if addr >= len(self.instrs) or addr < 0:
                self.ip += 1
                return 0
            instr = self.instrs[addr]
            if len(instr) == 2:
                if instr[0] == 'inc':
                    self.instrs[addr] = ('dec', ) + instr[1:]
                else:
                    self.instrs[addr] = ('inc', ) + instr[1:]
            elif len(instr) == 3:
                if instr[0] == 'jnz':
                    self.instrs[addr] = ('cpy', ) + instr[1:]
                else:
                    self.instrs[addr] = ('jnz',) + instr[1:]
            self.ip += 1
            return 0


instrs = read_input()
c = Computer(instrs)
c.registers['a'] = 7
c.run_to_end()
result = c.registers['a']
print(result)
