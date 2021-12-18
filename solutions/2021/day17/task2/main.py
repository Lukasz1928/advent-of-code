import re
from typing import Tuple

Pair = Tuple[int, int]


def parse_range(s: str) -> Tuple[str, Pair]:
    axis = s[0]
    l, r = s[2:].split('..')
    return axis, (int(l), int(r))


def read_input():
    with open('input', 'r') as f:
        raw = f.read()
    ranges = re.findall(r'\w=-?\d+..-?\d+', raw)
    parsed = [parse_range(r) for r in ranges]
    x_first = int(parsed[0][0] == 'x')
    return parsed[1 - x_first][1], parsed[x_first][1]


def shot_hits_target(initial: Pair, target: Tuple[Pair, Pair]) -> bool:
    position = (0, 0)
    velocity = initial
    while position[1] >= min(target[1]):
        position = (position[0] + velocity[0], position[1] + velocity[1])
        velocity = (v - 1 if (v := velocity[0]) > 0 else v + 1 if v < 0 else 0, velocity[1] - 1)
        if target[0][1] >= position[0] >= target[0][0] and target[1][1] >= position[1] >= target[1][0]:
            return True
    return False


target = read_input()

cnt = 0
for vx in range(target[0][1] + 1):
    for vy in range(-300, 301):
        hit = shot_hits_target((vx, vy), target)
        if hit:
            cnt += 1
print(cnt)
