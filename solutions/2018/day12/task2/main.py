

def read_input():
    with open('input', 'r') as f:
        lines = [l.strip().replace(' ', '') for l in f]
    ini = lines[0].split(':')[1]
    rules = []
    for r in lines[2:]:
        l, r = r.split('=>')
        rules.append((l, r))
    return rules, ini


def get_new_status(part, rules):
    for r in rules:
        if r[0] == part:
            return r[1]
    return None


class State:
    def __init__(self, initial_state, left=0):
        self.state = initial_state
        self.left = left

    def _fill(self):
        i = 0
        while i < min(5, len(self.state)) and self.state[i] == '.':
            i += 1
        j = 0
        while j < min(5, len(self.state)) and self.state[-j] == '.':
            j += 1
        self.left -= 5 - i
        self.state = '.' * (5 - i) + self.state + '.' * (5 - j)

    def _strip(self):
        i = 0
        while i < len(self.state) and self.state[i] == '.':
            i += 1
        j = 0
        while j < len(self.state) and self.state[-j] == '.':
            j += 1
        self.left += i
        self.state = self.state[i:-j + 1]

    def transform(self, rules):
        self._fill()
        transformed_state = ''
        for i in range(2, len(self.state) - 2):
            current_part = self.state[i - 2:i + 3]
            transformed_state += get_new_status(current_part, rules)
        self.left += 2
        self.state = transformed_state
        self._strip()


rules, raw_state = read_input()
state = State(raw_state)

seen_states = {state.state}
iter_number = 0
while True:
    state.transform(rules)
    ss = state.state
    iter_number += 1
    if ss in seen_states:
        break
    seen_states.add(ss)

iterations_to_do = 50000000000  # taken from task description
iterations_left = iterations_to_do - iter_number
left_index = state.left
pots_sum = 0
for idx, pot in enumerate(state.state, left_index):
    if pot == '#':
        pots_sum += iterations_left + idx
print(pots_sum)
