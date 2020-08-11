import re
from collections import defaultdict


class Instruction:
    def __init__(self, instr):
        pattern = '(?P<reg>\\w+) (?P<op>inc|dec) (?P<val>-?\\d+) if (?P<cond_reg>\\w+) (?P<comp_op>>|<|>=|<=|==|!=) (?P<cond_val>-?\\d+)'
        m = re.match(pattern, instr)
        self.register = m.group('reg')
        self.operation = m.group('op')
        self.change = int(m.group('val'))
        self.cond_left = m.group('cond_reg')
        self.comp_op = m.group('comp_op')
        self.cond_right = int(m.group('cond_val'))

    def apply(self, registers):
        lvalue = registers[self.cond_left]
        cond_str = "{} {} {}".format(lvalue, self.comp_op, self.cond_right)
        if eval(cond_str):
            if self.operation == 'inc':
                registers[self.register] += self.change
            else:
                registers[self.register] -= self.change


def read_input():
    with open('input', 'r') as f:
        lines = [l.strip() for l in f]
    return [Instruction(l) for l in lines]


regs = defaultdict(lambda: 0)
instrs = read_input()

max_value = 0
for i in instrs:
    i.apply(regs)
    m = max(regs.values())
    if m > max_value:
        max_value = m

print(max_value)
