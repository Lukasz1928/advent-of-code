import math


def read_input():
    with open('input', 'r') as f:
        return [l.strip() for l in f]


area_map = read_input()
trees = math.prod([sum(area_map[y][(y//slope[1] * slope[0]) % len(area_map[0])] == '#'
                   for y in range(0, len(area_map), slope[1])) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])
print(trees)
