from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def rotate(self, dir):
        if dir == 'left':
            if self == Direction.UP:
                return Direction.LEFT
            if self == Direction.DOWN:
                return Direction.RIGHT
            if self == Direction.LEFT:
                return Direction.DOWN
            if self == Direction.RIGHT:
                return Direction.UP
        if dir == 'right':
            if self == Direction.UP:
                return Direction.RIGHT
            if self == Direction.DOWN:
                return Direction.LEFT
            if self == Direction.LEFT:
                return Direction.UP
            if self == Direction.RIGHT:
                return Direction.DOWN
        if self == Direction.UP:
            return Direction.DOWN
        if self == Direction.DOWN:
            return Direction.UP
        if self == Direction.LEFT:
            return Direction.RIGHT
        if self == Direction.RIGHT:
            return Direction.LEFT


def move_position(pos, dir):
    if dir == Direction.UP:
        return pos[0] - 1, pos[1]
    if dir == Direction.DOWN:
        return pos[0] + 1, pos[1]
    if dir == Direction.LEFT:
        return pos[0], pos[1] - 1
    if dir == Direction.RIGHT:
        return pos[0], pos[1] + 1


def read_input():
    with open('input', 'r') as f:
        grid = [[1 if c == '#' else 0 for c in l.strip()] for l in f]
    return set((x, y) for x in range(len(grid)) for y in range(len(grid)) if grid[x][y] == 1), len(grid)


infected, size = read_input()
weakened = set()
flagged = set()

direction = Direction.UP
position = ((size - 1) // 2, (size - 1) // 2)
bursts = 10000000
infections = 0
for _ in range(bursts):
    if position in infected:
        direction = direction.rotate('right')
        flagged.add(position)
        infected.remove(position)
    elif position in weakened:
        infected.add(position)
        weakened.remove(position)
        infections += 1
    elif position in flagged:
        direction = direction.rotate('reverse')
        flagged.remove(position)
    else:  # clean node
        direction = direction.rotate('left')
        weakened.add(position)
    position = move_position(position, direction)

print(infections)
