import re
from ast import literal_eval


def parse_samples(samples):
    chunks = samples.split('\n\n')
    s = []
    for chunk in chunks:
        match = re.match(r'Before:\s*(?P<before>\[(?:\d+(?:,\s)?){4}\])\n(?P<instr>(?:\d+\s*){4})\nAfter:\s*(?P<after>\[(?:\d+(?:,\s)?){4}\])', chunk)
        s.append((tuple(literal_eval(match.group('before'))),
                  tuple(int(v) for v in match.group('instr').split(' ')),
                  tuple(literal_eval(match.group('after')))))
    return s


def parse_program(program):
    return [tuple(int(v) for v in line.split(' ')) for line in program.split('\n')]


def read_input():
    with open('input', 'r') as f:
        text = f.read()
    text_samples, text_program = text.split('\n\n\n\n')
    return parse_samples(text_samples), parse_program(text_program)


class Computer:

    instructions = ['addr', 'addi',
                    'mulr', 'muli',
                    'banr', 'bani',
                    'borr', 'bori',
                    'setr', 'seti',
                    'gtir', 'gtri', 'gtrr',
                    'eqir', 'eqri', 'eqrr']

    def __init__(self):
        self.registers = [0, 0, 0, 0]

    def apply_instruction(self, instr):
        if instr[0] == 'addr':
            self.registers[instr[3]] = self.registers[instr[1]] + self.registers[instr[2]]
        elif instr[0] == 'addi':
            self.registers[instr[3]] = self.registers[instr[1]] + instr[2]
        elif instr[0] == 'mulr':
            self.registers[instr[3]] = self.registers[instr[1]] * self.registers[instr[2]]
        elif instr[0] == 'muli':
            self.registers[instr[3]] = self.registers[instr[1]] * instr[2]
        elif instr[0] == 'banr':
            self.registers[instr[3]] = self.registers[instr[1]] & self.registers[instr[2]]
        elif instr[0] == 'bani':
            self.registers[instr[3]] = self.registers[instr[1]] & instr[2]
        elif instr[0] == 'borr':
            self.registers[instr[3]] = self.registers[instr[1]] | self.registers[instr[2]]
        elif instr[0] == 'bori':
            self.registers[instr[3]] = self.registers[instr[1]] | instr[2]
        elif instr[0] == 'setr':
            self.registers[instr[3]] = self.registers[instr[1]]
        elif instr[0] == 'seti':
            self.registers[instr[3]] = instr[1]
        elif instr[0] == 'gtir':
            self.registers[instr[3]] = int(instr[1] > self.registers[instr[2]])
        elif instr[0] == 'gtri':
            self.registers[instr[3]] = int(self.registers[instr[1]] > instr[2])
        elif instr[0] == 'gtrr':
            self.registers[instr[3]] = int(self.registers[instr[1]] > self.registers[instr[2]])
        elif instr[0] == 'eqir':
            self.registers[instr[3]] = int(instr[1] == self.registers[instr[2]])
        elif instr[0] == 'eqri':
            self.registers[instr[3]] = int(self.registers[instr[1]] == instr[2])
        elif instr[0] == 'eqrr':
            self.registers[instr[3]] = int(self.registers[instr[1]] == self.registers[instr[2]])
        return tuple(self.registers)


tests, _ = read_input()

comp = Computer()
count = 0

for test in tests:
    test_count = 0
    for instr in Computer.instructions:
        comp.registers = list(test[0])
        ret = comp.apply_instruction((instr, ) + test[1][1:])
        if ret == test[2]:
            test_count += 1
    if test_count >= 3:
        count += 1

print(count)
