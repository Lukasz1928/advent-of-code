from dataclasses import dataclass
from re import match


@dataclass(frozen=True)
class Machine:
    a: tuple[int, int]
    b: tuple[int, int]
    target: tuple[int, int]


def read_input() -> list[Machine]:
    with open('input', 'r') as f:
        raw = f.read()

    machines = []
    for group in raw.split('\n\n'):
        a_line, b_line, target_line = group.split('\n')
        a_match = match(r'Button A: X\+(?P<x_shift>\d+), Y\+(?P<y_shift>\d+)', a_line)
        b_match = match(r'Button B: X\+(?P<x_shift>\d+), Y\+(?P<y_shift>\d+)', b_line)
        target_match = match(r'Prize: X=(?P<x_target>\d+), Y=(?P<y_target>\d+)', target_line)

        machines.append(
            Machine(
                a=(int(a_match.group('x_shift')), int(a_match.group('y_shift'))),
                b=(int(b_match.group('x_shift')), int(b_match.group('y_shift'))),
                target=(int(target_match.group('x_target')), int(target_match.group('y_target'))),
            )
        )

    return machines


machines = read_input()

result = 0

for machine in machines:
    max_b = max(machine.target[0] // machine.b[0] + 1, machine.target[1] // machine.b[1] + 1)

    min_val = None

    for b_presses in range(max_b, -1, -1):
        leftover = machine.target[0] - b_presses * machine.b[0], machine.target[1] - b_presses * machine.b[1]
        if any(l < 0 for l in leftover):
            continue
        if any(l % m != 0 for l, m in zip(leftover, machine.a)):
            continue
        a_presses = leftover[0] // machine.a[0]
        if a_presses != leftover[1] // machine.a[1]:
            continue
        min_val = min(3 * a_presses + b_presses, min_val if min_val is not None else 3 * a_presses + b_presses)

    if min_val is not None:
        result += min_val

print(result)