import math


def read_input():
    with open('input', 'r') as f:
        return [(line[0], int(line[1:])) for line in f]


def rotate(point, angle):
    angle = math.radians(-angle)
    return (math.cos(angle) * point[0] - math.sin(angle) * point[1],
            math.sin(angle) * point[0] + math.cos(angle) * point[1])


class Ship:
    def __init__(self):
        self.location = (0, 0)
        self.waypoint = (10, 1)

    def move(self, instr):
        if instr[0] == 'N':
            self.waypoint = (self.waypoint[0], self.waypoint[1] + instr[1])
        elif instr[0] == 'S':
            self.waypoint = (self.waypoint[0], self.waypoint[1] - instr[1])
        elif instr[0] == 'E':
            self.waypoint = (self.waypoint[0] + instr[1], self.waypoint[1])
        elif instr[0] == 'W':
            self.waypoint = (self.waypoint[0] - instr[1], self.waypoint[1])
        elif instr[0] == 'L':
            self.waypoint = rotate(self.waypoint, -instr[1])
        elif instr[0] == 'R':
            self.waypoint = rotate(self.waypoint, instr[1])
        elif instr[0] == 'F':
            dx, dy = self.waypoint[0] * instr[1], self.waypoint[1] * instr[1]
            self.location = (self.location[0] + dx, self.location[1] + dy)


instructions = read_input()
ship = Ship()
for instr in instructions:
    ship.move(instr)
result = int(abs(ship.location[0]) + abs(ship.location[1]))
print(result)
