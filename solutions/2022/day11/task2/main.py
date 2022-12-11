from __future__ import annotations
import re
from functools import reduce


class Monkey:
    def __init__(self, items: list[int], op: str, test_value: int, if_true: int, if_false: int):
        self.items = items
        self.op = op
        self.test_val = test_value
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

    def process(self, monkeys: list[Monkey], mod_val: int):
        for item in self.items:
            self.inspected += 1
            val = eval(self.op.replace('old', str(item))) % mod_val
            target = self.if_true if val % self.test_val == 0 else self.if_false
            monkeys[target].add(val)
        self.items = []

    def add(self, item: int):
        self.items.append(item)


regex = r'Monkey (?P<id>\d+):\s*' \
        r'Starting items: (?P<items>.*?)\s*' \
        r'Operation: new = (?P<op>.*?)\s*' \
        r'Test: divisible by (?P<div>\d+)\s*' \
        r'If true: throw to monkey (?P<if_t>\d+)\s*' \
        r'If false: throw to monkey (?P<if_f>\d+)'


def read_input() -> list[Monkey]:
    data = []
    with open('input', 'r') as f:
        for monkey in f.read().split('\n\n'):
            x = re.match(regex, monkey)
            m = Monkey(items=[int(item) for item in x.group('items').split(', ')], op=x.group('op'),
                       test_value=int(x.group('div')), if_true=int(x.group('if_t')), if_false=int(x.group('if_f')))
            data.append(m)
    return data


monkeys_lst = read_input()
mod_val = reduce(lambda a, b: a * b, [m.test_val for m in monkeys_lst])
for _ in range(10000):
    for m in monkeys_lst:
        m.process(monkeys_lst, mod_val)

inspections = sorted([m.inspected for m in monkeys_lst])
result = inspections[-1] * inspections[-2]
print(result)

