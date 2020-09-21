

def read_input():
    with open('input', 'r') as f:
        return int(f.read().strip())


def is_open(x, y, number):
    if x < 0 or y < 0:
        return False
    s = x * x + 3 * x + 2 * x * y + y + y * y + number
    b = str(bin(s))[2:]
    return b.count('1') % 2 == 0


def neighbours(vertex, openf):
    nghs = set()
    if openf(vertex[0] - 1, vertex[1]):
        nghs.add((vertex[0] - 1, vertex[1]))
    if openf(vertex[0] + 1, vertex[1]):
        nghs.add((vertex[0] + 1, vertex[1]))
    if openf(vertex[0], vertex[1] - 1):
        nghs.add((vertex[0], vertex[1] - 1))
    if openf(vertex[0], vertex[1] + 1):
        nghs.add((vertex[0], vertex[1] + 1))
    return nghs


visited = set()
parents = dict()


def bfs(v, goal, openf):
    Q = []
    visited.add(v)
    Q.append(v)
    while len(Q) > 0:
        vert = Q.pop(0)
        if vert == goal:
            break
        for n in neighbours(vert, openf):
            if n not in visited:
                visited.add(n)
                parents[n] = vert
                Q.append(n)


def path_length(source, target, openf):
    bfs(source, target, openf)
    parents[source] = None
    c = target
    length = 0
    while parents[c] is not None:
        c = parents[c]
        length += 1
    return length


favourite_number = read_input()
open_function = lambda x, y: is_open(x, y, favourite_number)
target = (31, 39)
initial = (1, 1)
result = path_length(initial, target, open_function)
print(result)
