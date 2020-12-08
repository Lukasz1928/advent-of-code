
def read_input():
    with open('input', 'r') as f:
        lines = [line.strip().split() for line in f]
    return [(instr[0], int(instr[1])) for instr in lines]


class Computer:
    def __init__(self, program):
        self.program = program
        self.acc = 0
        self.ip = 0

    def run(self):
        executed = [False] * len(self.program)
        while True:
            if self.ip == len(self.program):
                return self.acc
            if executed[self.ip]:
                raise ValueError('Loop detected')
            executed[self.ip] = True
            self.execute_instruction()

    def execute_instruction(self):
        instr = self.program[self.ip]
        if instr[0] == 'acc':
            self.acc += instr[1]
            self.ip += 1
        elif instr[0] == 'jmp':
            self.ip += instr[1]
        elif instr[0] == 'nop':
            self.ip += 1
        else:
            raise ValueError('Invalid instruction')


def swap_instruction(prog, instr):
    if prog[instr][0] == 'acc':
        raise ValueError('cannot change instruction')
    new_instr = ('nop' if prog[instr][0] == 'jmp' else 'jmp', prog[instr][1])
    return prog[:instr] + [new_instr] + prog[instr + 1:]


program = read_input()
ret = None

for instr_id in range(len(program)):
    try:
        new_program = swap_instruction(program, instr_id)
    except ValueError:
        continue
    computer = Computer(new_program)
    try:
        ret = computer.run()
        break
    except (ValueError, IndexError):
        pass

print(ret)
