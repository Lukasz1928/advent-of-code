import re


class TM:
    def __init__(self, initial_state, steps, actions):
        self.tape = [0]
        self.position = 0
        self.actions = actions
        self.state = initial_state
        self.diagnostic_checksum_steps = steps
        self.step_count = 0

    def run(self):
        while self.step_count < self.diagnostic_checksum_steps:
            value = self.tape[self.position]
            state = self.state
            action = self.actions[(state, value)]
            self.tape[self.position] = action[0]
            self.position += (1 if action[1] == 'right' else -1)
            if self.position == -1:
                self.position = 0
                self.tape = [0] + self.tape
            elif self.position == len(self.tape):
                self.tape = self.tape + [0]
            self.state = action[2]
            self.step_count += 1
        return self.tape.count(1)

    @staticmethod
    def from_string(s):
        lines = s.split('\n')
        initial_state = lines[0][-2]
        checksum_step = int(re.findall(r'\d+', lines[1])[0])
        lines = [l.strip() for l in lines[3:]]

        instructions = dict()
        for i in range(0, len(lines), 10):
            state_lines = lines[i:i+9]
            state = re.match(r'In state (\w+):', state_lines[0]).group(1)

            write_value0 = int(re.match(r'- Write the value (\d+)\.', state_lines[2]).group(1))
            move_direction0 = re.match(r'- Move one slot to the (right|left)\.', state_lines[3]).group(1)
            next_state0 = re.match(r'- Continue with state (\w+)\.', state_lines[4]).group(1)

            write_value1 = int(re.match(r'- Write the value (\d+)\.', state_lines[6]).group(1))
            move_direction1 = re.match(r'- Move one slot to the (right|left)\.', state_lines[7]).group(1)
            next_state1 = re.match(r'- Continue with state (\w+)\.', state_lines[8]).group(1)

            instructions[(state, 0)] = (write_value0, move_direction0, next_state0)
            instructions[(state, 1)] = (write_value1, move_direction1, next_state1)

        return TM(initial_state, checksum_step, instructions)


def read_input():
    with open('input', 'r') as f:
        return TM.from_string(f.read())


machine = read_input()
result = machine.run()
print(result)
