import math


def read_input():
    with open('input', 'r') as f:
        lines = [l.split(' ') for l in f]
    ip = int(lines[0][1])
    return [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines[1:]], ip


class Computer:
    def __init__(self, ipr):
        self.registers = [0] * 6
        self.ipr = ipr
        self.ip = 0

    def run_instruction(self, program):
        if self.ip < 0 or self.ip >= len(program):
            return True
        instr = program[self.ip]
        self.registers[self.ipr] = self.ip
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
        self.ip = self.registers[self.ipr] + 1
        return False


def divisor_sum(number):
    sqr = int(math.sqrt(number))
    return sum(i + number // i for i in range(1, sqr + 1) if number % i == 0) - (sqr if sqr ** 2 == number else 0)


prog, ip = read_input()
comp = Computer(ip)
comp.registers[0] = 1
while comp.ip != 35:
    comp.run_instruction(prog)
comp.run_instruction(prog)
val = comp.registers[4]
result = divisor_sum(val)
print(result)

