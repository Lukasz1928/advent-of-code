from __future__ import annotations

from collections import Counter
from enum import Enum


T = tuple[int, int]


class Direction(Enum):
    E = "e"
    SE = "se"
    SW = "sw"
    W = "w"
    NW = "nw"
    NE = "ne"

    @classmethod
    def get_directions(cls, seq: str) -> list[Direction]:
        dirs = []
        while seq:
            try:
                d = Direction[seq[:2].upper()]
                seq = seq[2:]
            except KeyError:
                d = Direction[seq[0].upper()]
                seq = seq[1:]
            dirs.append(d)
        return dirs


def read_input() -> list[list[Direction]]:
    with open('input', 'r') as f:
        raw_input = [line.strip() for line in f.readlines()]
    return [Direction.get_directions(line) for line in raw_input]


def reduce_directions(dirs: list[Direction]) -> T:
    cnts = Counter(dirs)
    count_e = cnts[Direction.E] - cnts[Direction.W]
    count_se = cnts[Direction.SE] - cnts[Direction.NW]
    count_ne = cnts[Direction.NE] - cnts[Direction.SW]
    m = min(count_se, count_ne)
    e = count_e + m
    if count_ne >= count_se:
        return e, count_ne - count_se
    return e + (count_se - count_ne), count_ne - count_se


def neighbors(location: T) -> list[T]:
    changes = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]
    return [(location[0] + c[0], location[1] + c[1]) for c in changes]


def count_black_neighbors(location: T, blacks: set[T]) -> int:
    return len([n for n in neighbors(location) if n in blacks])


def step(blacks: set[T]) -> set[T]:
    new_blacks = set(blacks)
    checked_whites = set()
    for b in blacks:
        if (cnt := count_black_neighbors(b, blacks)) == 0 or cnt > 2:
            new_blacks.remove(b)
        for ngh in neighbors(b):
            if ngh in checked_whites:
                continue
            checked_whites.add(ngh)
            if ngh not in blacks and ngh not in new_blacks and count_black_neighbors(ngh, blacks) == 2:
                new_blacks.add(ngh)
    return new_blacks


directions = read_input()
reduced = [reduce_directions(dirs) for dirs in directions]
cnt = Counter(reduced)

black_tiles = {k for k, v in cnt.items() if v % 2 == 1}

days_count = 100
for _ in range(days_count):
    black_tiles = step(black_tiles)

result = len(black_tiles)
print(result)
