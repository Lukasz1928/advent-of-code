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
        if self == Direction.UP:
            return Direction.RIGHT
        if self == Direction.DOWN:
            return Direction.LEFT
        if self == Direction.LEFT:
            return Direction.UP
        if self == Direction.RIGHT:
            return Direction.DOWN


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
direction = Direction.UP
position = ((size - 1) // 2, (size - 1) // 2)
bursts = 10000
infections = 0
for b in range(bursts):
    if position in infected:
        direction = direction.rotate('right')
        infected.remove(position)
    else:
        direction = direction.rotate('left')
        infected.add(position)
        infections += 1
    position = move_position(position, direction)

print(infections)
