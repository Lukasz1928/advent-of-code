from copy import copy
from enum import Enum, IntEnum


class IntcodeCodes(Enum):
    HALT = 0,
    NO_INPUT = 1,
    RET = 2

class Defaultlist:
    def __init__(self, init_values):
        self.values = copy(init_values)

    def __getitem__(self, item):
        if type(item) is slice:
            if item.stop is not None and item.stop >= len(self.values):
                missing_length = item.stop - len(self.values) + 1
                print(missing_length)
                self.values.extend([0] * missing_length)
        elif item >= len(self.values):
            missing_length = item - len(self.values) + 1
            self.values.extend([0] * missing_length)
        return self.values[item]

    def __setitem__(self, key, value):
        if key < len(self.values):
            self.values[key] = value
        else:
            missing_length = key - len(self.values) + 1
            self.values.extend([0] * missing_length)
            self.values[key] = value

class IntcodeComputer:
    def __init__(self, program):
        self.program = Defaultlist(program)
        self.ip = 0
        self.relative_base = 0

    class ParameterMode(IntEnum):
        POSITION = 0,
        IMMEDIATE = 1,
        RELATIVE = 2

    def _get_parameter(self, addr, mode):
        if mode == IntcodeComputer.ParameterMode.POSITION:
            return self.program[self.program[addr]]
        if mode == IntcodeComputer.ParameterMode.IMMEDIATE:
            return self.program[addr]
        if mode == IntcodeComputer.ParameterMode.RELATIVE:
            return self.program[self.relative_base + self.program[addr]]

    def run(self, pin=None):
        while True:
            p1, p2, p3, op = IntcodeComputer.decode(self.program[self.ip])
            if op == 99:  # end of program
                return IntcodeCodes.HALT, -1
            if op == 1:  # addition
                if p3 == IntcodeComputer.ParameterMode.POSITION:
                    self.program[self.program[self.ip + 3]] = self._get_parameter(self.ip + 1, p1) + self._get_parameter(self.ip + 2, p2)
                elif p3 == IntcodeComputer.ParameterMode.RELATIVE:
                    self.program[self.relative_base + self.program[self.ip + 3]] = self._get_parameter(self.ip + 1, p1) + self._get_parameter(self.ip + 2, p2)
                self.ip += 4
            elif op == 2:  # multiplication
                if p3 == IntcodeComputer.ParameterMode.POSITION:
                    self.program[self.program[self.ip + 3]] = self._get_parameter(self.ip + 1, p1) * self._get_parameter(self.ip + 2, p2)
                elif p3 == IntcodeComputer.ParameterMode.RELATIVE:
                    self.program[self.relative_base + self.program[self.ip + 3]] = self._get_parameter(self.ip + 1, p1) * self._get_parameter(self.ip + 2, p2)
                self.ip += 4
            elif op == 3:  # read input
                if pin is not None:
                    if p1 == IntcodeComputer.ParameterMode.POSITION:
                        self.program[self.program[self.ip + 1]] = pin
                    elif p1 == IntcodeComputer.ParameterMode.RELATIVE:
                        self.program[self.relative_base + self.program[self.ip + 1]] = pin
                    pin = None
                    self.ip += 2
                else:
                    return IntcodeCodes.NO_INPUT, -1
            elif op == 4:  # write to output
                res = self._get_parameter(self.ip + 1, p1)
                self.ip += 2
                return IntcodeCodes.RET, res
            elif op == 5:  # jump if true
                if self._get_parameter(self.ip + 1, p1) != 0:
                    self.ip = self._get_parameter(self.ip + 2, p2)
                else:
                    self.ip += 3
            elif op == 6:  # jump if false
                if self._get_parameter(self.ip + 1, p1) == 0:
                    self.ip = self._get_parameter(self.ip + 2, p2)
                else:
                    self.ip += 3
            elif op == 7:  # less than
                if p3 == IntcodeComputer.ParameterMode.POSITION:
                    self.program[self.program[self.ip + 3]] = 1 if self._get_parameter(self.ip + 1, p1) < self._get_parameter(self.ip + 2, p2) else 0
                elif p3 == IntcodeComputer.ParameterMode.RELATIVE:
                    self.program[self.relative_base + self.program[self.ip + 3]] = 1 if self._get_parameter(self.ip + 1, p1) < self._get_parameter(self.ip + 2, p2) else 0
                self.ip += 4
            elif op == 8:  # equals
                if p3 == IntcodeComputer.ParameterMode.POSITION:
                    self.program[self.program[self.ip + 3]] = 1 if self._get_parameter(self.ip + 1, p1) == self._get_parameter(self.ip + 2, p2) else 0
                elif p3 == IntcodeComputer.ParameterMode.RELATIVE:
                    self.program[self.relative_base + self.program[self.ip + 3]] = 1 if self._get_parameter(self.ip + 1, p1) == self._get_parameter(self.ip + 2, p2) else 0
                self.ip += 4
            elif op == 9:  # adjust relative base
                self.relative_base += self._get_parameter(self.ip + 1, p1)
                self.ip += 2

    @staticmethod
    def decode(inst):
        s = str(inst).zfill(5)
        p1 = IntcodeComputer.ParameterMode(int(s[2]))
        p2 = IntcodeComputer.ParameterMode(int(s[1]))
        p3 = IntcodeComputer.ParameterMode(int(s[0]))
        op = int(s[3:])
        return p1, p2, p3, op


prog = [int(x) for x in open('input', 'r').read().split(',')]
comp = IntcodeComputer(prog)
r = []
i = 0
while True:
    status, ret = comp.run(2 if i == 0 else None)
    if status == IntcodeCodes.HALT:
        break
    r.append(ret)
    i = 1
print(r[0])
