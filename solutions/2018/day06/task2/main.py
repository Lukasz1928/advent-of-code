from collections import deque


def read_input():
    with open('input', 'r') as f:
        return [(int(c[0]), int(c[1])) for c in [l.replace(' ', '').split(',') for l in f]]


def distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def is_within_distance(x, y, coords, max_distance):
    return sum(distance((x, y), c) for c in coords) < max_distance


def find_any_within_distance(mx, my, coords, max_distance):
    for y in range(my + 2):
        for x in range(mx + 2):
            if is_within_distance(x, y, coords, max_distance):
                return x, y


def neighbours(x, y):
    funs = [lambda p, q: (p + 1, q),
            lambda p, q: (p - 1, q),
            lambda p, q: (p, q + 1),
            lambda p, q: (p, q - 1)]
    for f in funs:
        yield f(x, y)


coords = read_input()
maxx, maxy = max(x[0] for x in coords), max(x[1] for x in coords)
max_total_distance = 10000

initial = find_any_within_distance(maxx, maxy, coords, max_total_distance)
Q = deque([initial])
visited = {initial}
while len(Q) > 0:
    v = Q.popleft()
    for ngh in neighbours(v[0], v[1]):
        if ngh not in visited and is_within_distance(ngh[0], ngh[1], coords, max_total_distance):
            visited.add(ngh)
            Q.append(ngh)

result = len(visited)
print(result)
