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


directions = read_input()
reduced = [reduce_directions(dirs) for dirs in directions]
cnt = Counter(reduced)

black_tiles_count = len([v for v in cnt.values() if v % 2 == 1])
print(black_tiles_count)
