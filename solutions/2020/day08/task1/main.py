
def read_input():
    with open('input', 'r') as f:
        return Computer.from_text([line.strip() for line in f])


class Computer:
    def __init__(self, program):
        self.program = program
        self.acc = 0
        self.ip = 0

    def run(self):
        executed = [False] * len(self.program)
        while not executed[self.ip]:
            executed[self.ip] = True
            self.execute_instruction()
        return self.acc

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

    @staticmethod
    def from_text(lines):
        prog = [line.split() for line in lines]
        return Computer([(instr[0], int(instr[1])) for instr in prog])


computer = read_input()
result = computer.run()
print(result)
