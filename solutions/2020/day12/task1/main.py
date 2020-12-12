import math


def read_input():
    with open('input', 'r') as f:
        return [(line[0], int(line[1:])) for line in f]


class Ship:
    def __init__(self):
        self.location = (0, 0)
        self.angle = 90

    def move(self, instr):
        if instr[0] == 'N':
            self.location = (self.location[0], self.location[1] + instr[1])
        elif instr[0] == 'S':
            self.location = (self.location[0], self.location[1] - instr[1])
        elif instr[0] == 'E':
            self.location = (self.location[0] + instr[1], self.location[1])
        elif instr[0] == 'W':
            self.location = (self.location[0] - instr[1], self.location[1])
        elif instr[0] == 'L':
            self.angle = (self.angle - instr[1]) % 360
        elif instr[0] == 'R':
            self.angle = (self.angle + instr[1]) % 360
        elif instr[0] == 'F':
            self.location = (self.location[0] + math.sin(math.radians(self.angle)) * instr[1],
                             self.location[1] + math.cos(math.radians(self.angle)) * instr[1])


instructions = read_input()
ship = Ship()
for instr in instructions:
    ship.move(instr)
result = int(abs(ship.location[0]) + abs(ship.location[1]))
print(result)
