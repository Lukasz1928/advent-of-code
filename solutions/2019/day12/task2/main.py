import math

import regex
import numpy as np


class Moon:
    def __init__(self, pos):
        self.position = np.asarray(pos).astype(np.int)
        self.velocity = np.zeros((3,)).astype(np.int)

    @staticmethod
    def from_string(s):
        r = regex.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', s)
        pos = [int(r[1]), int(r[2]), int(r[3])]
        return Moon(pos)

    def change_velocity(self, other):
        self.velocity += np.vectorize(lambda x: 0 if x == 0 else -1 if x > 0 else 1)(self.position - other.position)

    def change_position(self):
        self.position += self.velocity


def find_period(moons, axis):
    init_pos = tuple(m.position[axis] for m in moons)
    steps = 0
    while True:
        for m1 in moons:
            for m2 in moons:
                if m1 != m2:
                    m1.change_velocity(m2)
        for m in moons:
            m.change_position()
        steps += 1
        if tuple(m.position[axis] for m in moons) == init_pos and all(m.velocity[axis] == 0 for m in moons):
            return steps


def lcm(a, b, c=None):
    if c is None:
        return a * b / math.gcd(int(a), int(b))
    return int(lcm(a, lcm(b, c)))


lines = open('input', 'r').read().splitlines()

periods = [find_period([Moon.from_string(s) for s in lines], i) for i in range(3)]
print(lcm(*periods))
