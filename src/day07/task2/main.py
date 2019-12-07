from copy import copy
from enum import Enum


class IntcodeCodes(Enum):
    HALT = 0,
    NO_INPUT = 1,
    RET = 2

class IncodeComputer:
    def __init__(self, program):
        self.program = copy(program)
        self.ip = 0

    def run(self, pin=None):
        while True:
            p1, p2, p3, op = IncodeComputer.decode(self.program[self.ip])
            if op == 99:  # end of program
                return IntcodeCodes.HALT, -1
            if op == 1:  # addition
                self.program[self.program[self.ip + 3]] = ((self.program[self.program[self.ip + 1]] if p1 else self.program[self.ip + 1]) + (self.program[self.program[self.ip + 2]] if p2 else self.program[self.ip + 2]))
                self.ip += 4
            elif op == 2:  # multiplication
                self.program[self.program[self.ip + 3]] = ((self.program[self.program[self.ip + 1]] if p1 else self.program[self.ip + 1]) * (self.program[self.program[self.ip + 2]] if p2 else self.program[self.ip + 2]))
                self.ip += 4
            elif op == 3:  # read input
                if pin is not None:
                    self.program[self.program[self.ip + 1]] = pin
                    pin = None
                    self.ip += 2
                else:
                    return IntcodeCodes.NO_INPUT, -1
            elif op == 4:  # write to output
                res = self.program[self.program[self.ip + 1]] if p1 else self.program[self.ip + 1]
                self.ip += 2
                return IntcodeCodes.RET, res
            elif op == 5:  # jump if true
                if (self.program[self.program[self.ip + 1]] if p1 else self.program[self.ip + 1]) != 0:
                    self.ip = self.program[self.program[self.ip + 2]] if p2 else self.program[self.ip + 2]
                else:
                    self.ip += 3
            elif op == 6:  # jump if false
                if (self.program[self.program[self.ip + 1]] if p1 else self.program[self.ip + 1]) == 0:
                    self.ip = self.program[self.program[self.ip + 2]] if p2 else self.program[self.ip + 2]
                else:
                    self.ip += 3
            elif op == 7:  # less than
                self.program[self.program[self.ip + 3]] = 1 if ((self.program[self.program[self.ip + 1]] if p1 else self.program[self.ip + 1]) < (self.program[self.program[self.ip + 2]] if p2 else self.program[self.ip + 2])) else 0
                self.ip += 4
            elif op == 8:  # equals
                self.program[self.program[self.ip + 3]] = 1 if ((self.program[self.program[self.ip + 1]] if p1 else self.program[self.ip + 1]) == (self.program[self.program[self.ip + 2]] if p2 else self.program[self.ip + 2])) else 0
                self.ip += 4

    @staticmethod
    def decode(inst):
        s = str(inst).zfill(5)
        p1 = s[2] == '0'
        p2 = s[1] == '0'
        p3 = s[0] == '0'
        op = int(s[3:])
        return p1, p2, p3, op


perms = []
def permutate(digits, current=""):
    if len(digits) == 0:
        perms.append(current)
    else:
        for digit in digits:
            permutate([x for x in digits if x != digit], current + digit)
permutate(['5', '6', '7', '8', '9'])

prog_ = [int(x) for x in open('input', 'r').read().split(',')]

m = -1
for perm in perms:
    inp = 0
    code = 3
    comps = [IncodeComputer(prog_) for _ in range(5)]
    for i, c in enumerate(comps):
        c.run(int(perm[i]))
    comp_id = 0
    last_out = 0
    while True:
        c, r = comps[comp_id].run(inp)
        if c == IntcodeCodes.RET:
            inp = r
            if comp_id == 4:
                last_out = r
        elif c == IntcodeCodes.NO_INPUT:
            pass
        elif c == IntcodeCodes.HALT:
            break
        comp_id = (comp_id + 1) % 5
    if last_out > m:
        m = last_out
print(m)
