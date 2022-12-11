instruction = tuple[str, int | None]


def read_input() -> list[instruction]:
    with open('input', 'r') as f:
        return [((tokens := line.strip().split())[0], int(tokens[1]) if len(tokens) > 1 else None) for line in f]


class Cpu:
    def __init__(self, instr: list[instruction], register: int = 1):
        self._instr = instr
        self._register = register
        self._image = []
        self._cycle = 1

    def execute(self):
        for ins in self._instr:
            if ins[0] == 'noop':
                self._handle_cycle()
            else:  # addx
                self._handle_cycle()
                self._handle_cycle()
                self._register += ins[1]

    def _handle_cycle(self):
        self._image.append('#' if self._register - 1 <= (self._cycle - 1) % 40 <= self._register + 1 else ' ')
        self._cycle += 1

    def print_image(self):
        width = 40
        for idx, val in enumerate(self._image):
            if idx > 0 and idx % width == 0:
                print()
            print(val, end='')


instructions = read_input()
cpu = Cpu(instructions)
cpu.execute()
cpu.print_image()
