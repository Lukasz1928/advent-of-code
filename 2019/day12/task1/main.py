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

    def energy(self):
        return np.sum(np.abs(self.position)) * np.sum(np.abs(self.velocity))


moons = [Moon.from_string(s) for s in open('input', 'r').read().splitlines()]

steps = 1000
for i in range(steps):
    for m1 in moons:
        for m2 in moons:
            if m1 != m2:
                m1.change_velocity(m2)
    for m in moons:
        m.change_position()

print(sum(m.energy() for m in moons))
