from __future__ import annotations
from enum import Enum


def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

    def rotate(self) -> Direction:
        return {
            self.UP: self.RIGHT,
            self.DOWN: self.LEFT,
            self.LEFT: self.UP,
            self.RIGHT: self.DOWN
        }[self]

    def move_direction(self) -> tuple[int, int]:
        return {
            self.UP: (-1, 0),
            self.DOWN: (1, 0),
            self.LEFT: (0, -1),
            self.RIGHT: (0, 1),
        }[self]


def find_start(g: list[str]) -> tuple[tuple[int, int], Direction]:
    for row_idx, row in enumerate(g):
        for col_idx, elem in enumerate(row):
            if elem == '^':
                return (row_idx, col_idx), Direction.UP
            if elem == 'v':
                return (row_idx, col_idx), Direction.DOWN
            if elem == '>':
                return (row_idx, col_idx), Direction.RIGHT
            if elem == '<':
                return (row_idx, col_idx), Direction.LEFT


def move_position(pos: tuple[int, int], direction: Direction) -> tuple[int, int]:
    md = direction.move_direction()
    return pos[0] + md[0], pos[1] + md[1]


grid = read_input()
size = len(grid), len(grid[0])

position, direction = find_start(grid)
visited = set()
while True:
    visited.add(position)
    next_position = move_position(position, direction)
    if not (0 <= next_position[0] < size[0] and 0 <= next_position[1] < size[1]):
        break
    if grid[next_position[0]][next_position[1]] == '#':
        direction = direction.rotate()
    else:
        position = next_position

result = len(visited)
print(result)
