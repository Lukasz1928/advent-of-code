instruction = tuple[str, int | None]


def read_input() -> list[instruction]:
    with open('input', 'r') as f:
        return [((tokens := line.strip().split())[0], int(tokens[1]) if len(tokens) > 1 else None) for line in f]


class Cpu:
    def __init__(self, instr: list[instruction], register: int = 1):
        self._instr = instr
        self._register = register
        self._values: list[int] = []

    def execute(self):
        for ins in self._instr:
            if ins[0] == 'noop':
                self._values.append(self._register)
            else:  # addx
                self._values.extend([self._register] * 2)
                self._register += ins[1]

    def value(self) -> int:
        res = 0
        idx = 19
        while idx < len(self._values):
            res += (idx + 1) * self._values[idx]
            idx += 40
        return res


instructions = read_input()
cpu = Cpu(instructions)
cpu.execute()
result = cpu.value()
print(result)
