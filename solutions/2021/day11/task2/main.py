from collections import deque


def read_input():
    with open('input', 'r') as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]


def nghs(x, y, size=10):
    for dx in {-1, 0, 1}:
        for dy in {-1, 0, 1}:
            if (dx != 0 or dy != 0) and 0 <= x + dx < size and 0 <= y + dy < size:
                yield x + dx, y + dy


def step(lvls):
    lvls = [[elem + 1 for elem in row] for row in lvls]
    flashed = set()
    to_flash = deque([(i, j) for i in range(len(lvls)) for j in range(len(lvls[i])) if lvls[i][j] > 9])
    while to_flash:
        current = to_flash.pop()
        flashed.add(current)
        for ngh in nghs(*current):
            lvls[ngh[0]][ngh[1]] += 1
            if lvls[ngh[0]][ngh[1]] > 9 and ngh not in flashed and ngh not in to_flash:
                to_flash.append(ngh)
    for f in flashed:
        lvls[f[0]][f[1]] = 0
    return lvls, len(flashed)


levels = read_input()
size = len(levels) * len(levels[0])
step_number = 0
while True:
    levels, f = step(levels)
    step_number += 1
    if f == size:
        break
print(step_number)
