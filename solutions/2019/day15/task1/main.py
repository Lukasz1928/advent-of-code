from copy import copy
from enum import Enum, IntEnum


class IntcodeCodes(Enum):
    HALT = 0,
    NO_INPUT = 1,
    RET = 2


class Defaultlist:
    def __init__(self, init_values):
        self.values = copy(init_values)

    def __getitem__(self, item):
        if type(item) is slice:
            if item.stop is not None and item.stop >= len(self.values):
                missing_length = item.stop - len(self.values) + 1
                print(missing_length)
                self.values.extend([0] * missing_length)
        elif item >= len(self.values):
            missing_length = item - len(self.values) + 1
            self.values.extend([0] * missing_length)
        return self.values[item]

    def __setitem__(self, key, value):
        if key < len(self.values):
            self.values[key] = value
        else:
            missing_length = key - len(self.values) + 1
            self.values.extend([0] * missing_length)
            self.values[key] = value


class IntcodeComputer:
    def __init__(self, program):
        self.program = Defaultlist(program)
        self.ip = 0
        self.relative_base = 0

    class ParameterMode(IntEnum):
        POSITION = 0,
        IMMEDIATE = 1,
        RELATIVE = 2

    def _get_parameter(self, addr, mode):
        if mode == IntcodeComputer.ParameterMode.POSITION:
            return self.program[self.program[addr]]
        if mode == IntcodeComputer.ParameterMode.IMMEDIATE:
            return self.program[addr]
        if mode == IntcodeComputer.ParameterMode.RELATIVE:
            return self.program[self.relative_base + self.program[addr]]

    def run(self, pin=None):
        while True:
            p1, p2, p3, op = IntcodeComputer.decode(self.program[self.ip])
            if op == 99:  # end of program
                return IntcodeCodes.HALT, -1
            if op == 1:  # addition
                if p3 == IntcodeComputer.ParameterMode.POSITION:
                    self.program[self.program[self.ip + 3]] = self._get_parameter(self.ip + 1, p1) + self._get_parameter(self.ip + 2, p2)
                elif p3 == IntcodeComputer.ParameterMode.RELATIVE:
                    self.program[self.relative_base + self.program[self.ip + 3]] = self._get_parameter(self.ip + 1, p1) + self._get_parameter(self.ip + 2, p2)
                self.ip += 4
            elif op == 2:  # multiplication
                if p3 == IntcodeComputer.ParameterMode.POSITION:
                    self.program[self.program[self.ip + 3]] = self._get_parameter(self.ip + 1, p1) * self._get_parameter(self.ip + 2, p2)
                elif p3 == IntcodeComputer.ParameterMode.RELATIVE:
                    self.program[self.relative_base + self.program[self.ip + 3]] = self._get_parameter(self.ip + 1, p1) * self._get_parameter(self.ip + 2, p2)
                self.ip += 4
            elif op == 3:  # read input
                if pin is not None:
                    if p1 == IntcodeComputer.ParameterMode.POSITION:
                        self.program[self.program[self.ip + 1]] = pin
                    elif p1 == IntcodeComputer.ParameterMode.RELATIVE:
                        self.program[self.relative_base + self.program[self.ip + 1]] = pin
                    pin = None
                    self.ip += 2
                else:
                    return IntcodeCodes.NO_INPUT, -1
            elif op == 4:  # write to output
                res = self._get_parameter(self.ip + 1, p1)
                self.ip += 2
                return IntcodeCodes.RET, res
            elif op == 5:  # jump if true
                if self._get_parameter(self.ip + 1, p1) != 0:
                    self.ip = self._get_parameter(self.ip + 2, p2)
                else:
                    self.ip += 3
            elif op == 6:  # jump if false
                if self._get_parameter(self.ip + 1, p1) == 0:
                    self.ip = self._get_parameter(self.ip + 2, p2)
                else:
                    self.ip += 3
            elif op == 7:  # less than
                if p3 == IntcodeComputer.ParameterMode.POSITION:
                    self.program[self.program[self.ip + 3]] = 1 if self._get_parameter(self.ip + 1, p1) < self._get_parameter(self.ip + 2, p2) else 0
                elif p3 == IntcodeComputer.ParameterMode.RELATIVE:
                    self.program[self.relative_base + self.program[self.ip + 3]] = 1 if self._get_parameter(self.ip + 1, p1) < self._get_parameter(self.ip + 2, p2) else 0
                self.ip += 4
            elif op == 8:  # equals
                if p3 == IntcodeComputer.ParameterMode.POSITION:
                    self.program[self.program[self.ip + 3]] = 1 if self._get_parameter(self.ip + 1, p1) == self._get_parameter(self.ip + 2, p2) else 0
                elif p3 == IntcodeComputer.ParameterMode.RELATIVE:
                    self.program[self.relative_base + self.program[self.ip + 3]] = 1 if self._get_parameter(self.ip + 1, p1) == self._get_parameter(self.ip + 2, p2) else 0
                self.ip += 4
            elif op == 9:  # adjust relative base
                self.relative_base += self._get_parameter(self.ip + 1, p1)
                self.ip += 2

    @staticmethod
    def decode(inst):
        s = str(inst).zfill(5)
        p1 = IntcodeComputer.ParameterMode(int(s[2]))
        p2 = IntcodeComputer.ParameterMode(int(s[1]))
        p3 = IntcodeComputer.ParameterMode(int(s[0]))
        op = int(s[3:])
        return p1, p2, p3, op

directions = [0, 1, 2, 3]
directions_changes = [(0, 1), (0, -1), (-1, 0), (1, 0)]

class Vertex:
    def __init__(self, c):
        self.coords = c
        self.neighbour_checked = [False, False, False, False]
        self.neighbours = [None, None, None, None]

    def __hash__(self):
        return 10000 * self.coords[0] + self.coords[1]

    def add_neighbour(self, direction, type):
        self.neighbour_checked[direction] = True
        self.neighbours[direction] = None


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_vertex(self, v):
        self.vertices.add(v)
        self.edges[v] = []

    def add_egde(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.edges[v1] = v2
        self.edges[v2] = v1

    def get_vertex(self, loc):
        try:
            return [x for x in self.vertices if x.coords == loc][0]
        except KeyError:
            return None


prog = [int(x) for x in open('input', 'r').read().split(',')]
comp = IntcodeComputer(prog)


def move(pt, dir):
    return tuple(pt[i] + directions_changes[dir][i] for i in range(2))


location = (0, 0)
g = Graph()
g.add_vertex(Vertex(location))

while True:
    current = g.get_vertex(location)
    for direction in directions:
        s, r = comp.run(direction)
        new_location = move(location, direction)
        if not current.neighbour_checked[direction]:
            if s == IntcodeCodes.RET:
                if r == 0: # wall
                    current.neighbour_visited[direction] = True

            else:
                print('dupa')

