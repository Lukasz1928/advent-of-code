import re


def parse_input(instrs):
    initials = {}
    rules = {}
    for i in instrs:
        p = "value (\\d+) goes to bot (\\d+)"
        m = re.match(p, i)
        if m is not None:
            v = int(m.group(1))
            b = int(m.group(2))
            if b in initials.keys():
                initials[b].append(v)
            else:
                initials[b] = [v]
        else:
            p = "bot (\\d+) gives low to (bot|output) (\\d+) and high to (bot|output) (\\d+)"
            m = re.match(p, i)
            b = int(m.group(1))
            out1 = m.group(2)
            out1_id = int(m.group(3))
            out2 = m.group(4)
            out2_id = int(m.group(5))
            rules[b] = {
                'low': (out1, out1_id),
                'high': (out2, out2_id)
            }
    return initials, rules


class Outputs:
    def __init__(self):
        self.values = {}

    def add(self, output, value):
        if output in self.values.keys():
            self.values[output].append(value)
        else:
            self.values[output] = [value]


class Bot:
    def __init__(self, bot_id, chips, rules, outputs):
        self.id = bot_id
        self.chips = chips
        self.rules = rules
        self.bots = {}
        self.outputs = outputs

    def receive(self, chip=None):
        if chip is not None:
            self.chips.append(chip)
        if len(self.chips) == 2:
            low = min(self.chips)
            high = max(self.chips)
            self.chips = []
            if self.rules['low'][0] == 'bot':
                self.bots[self.rules['low'][1]].receive(low)
            else:
                self.outputs.add(self.rules['low'][1], low)
            if self.rules['high'][0] == 'bot':
                self.bots[self.rules['high'][1]].receive(high)
            else:
                self.outputs.add(self.rules['high'][1], high)

    def initialize(self, all_bots):
        self.bots = all_bots


def solve(ini, rules):
    out = Outputs()
    bot_ids = set(ini.keys()) | set(rules.keys())
    bots = {i: Bot(i, ini[i] if i in ini.keys() else [], rules[i], out) for i in bot_ids}
    for b in bots.values():
        b.initialize(bots)
    start_bot = [b for b in bots.values() if len(b.chips) == 2][0]
    start_bot.receive()

    p = 1
    for output_id in [0, 1, 2]:
        for v in out.values[output_id]:
            p *= v
    return p


with open('input', 'r') as f:
    instrs = [l.strip() for l in f]

initials, rules = parse_input(instrs)

result = solve(initials, rules)
print(result)
