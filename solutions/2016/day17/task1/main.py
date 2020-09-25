from collections import deque
from hashlib import md5


def read_input():
    with open('input', 'r') as f:
        return f.read().strip()


directions = ['U', 'D', 'L', 'R']


def possible_directions(loc):
    dirs = set()
    if loc[0] > 0:
        dirs.add('L')
    if loc[0] < 3:
        dirs.add('R')
    if loc[1] > 0:
        dirs.add('U')
    if loc[1] < 3:
        dirs.add('D')
    return dirs


def move_location(loc, dir):
    if dir == 'U':
        return loc[0], loc[1] - 1
    if dir == 'D':
        return loc[0], loc[1] + 1
    if dir == 'L':
        return loc[0] - 1, loc[1]
    if dir == 'R':
        return loc[0] + 1, loc[1]


def doors_open(passcode, path):
    m = md5()
    m.update((passcode + path).encode('utf-8'))
    h = m.hexdigest()[:4]
    return {d: h[i] in {'b', 'c', 'd', 'e', 'f'} for i, d in enumerate(directions)}


def direction(p1, p2):
    d = (p2[0] - p1[0], p2[1] - p1[1])
    if d == (0, 1):
        return "R"
    if d == (0, -1):
        return "L"
    if d == (1, 0):
        return "D"
    if d == (-1, 0):
        return "U"


def find_shortest_path(start, target, passcode):
    Q = deque()
    visited = {start}
    paths = {start: ""}
    Q.append(start)
    parents = {start: None}
    while len(Q) > 0:
        v = Q.popleft()
        if v == target:
            path = ""
            c = target
            while paths[c] != "":
                path += direction(parents[c], c)
                c = parents[c]
            return path
        open_doors = doors_open(passcode, paths[v])
        for d in possible_directions(v):
            if open_doors[d]:
                ngh = move_location(v, d)
                if ngh not in visited:
                    visited.add(ngh)
                    paths[ngh] = paths[v] + d
                    parents[ngh] = v
                    Q.append(ngh)


passcode = read_input()

start = (0, 0)
target = (3, 3)

path = find_shortest_path(start, target, passcode)
print(path)