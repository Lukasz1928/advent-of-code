# a little bit overkill but it's nice
import functools
import z3


def read_input():
    with open('input', 'r') as f:
        return {int(line) for line in f}


def in_set(value, values):
    return z3.Or([v == value for v in values])


expenses_report = read_input()
entries_count = 3

solver = z3.Solver()
entries = [z3.Int(f'e{i}') for i in range(entries_count)]
solver.add(sum(entries) == 2020)
for e in entries:
    solver.add(in_set(e, expenses_report))

solver.check()

entries_value = [solver.model()[e].as_long() for e in entries]
result = functools.reduce(lambda acc, val: acc * val, entries_value)
print(result)
