

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
distances = {}


def bfs(v, openf):
    Q = []
    visited.add(v)
    Q.append(v)
    while len(Q) > 0:
        vert = Q.pop(0)
        if distances[vert] < 50:
            for n in neighbours(vert, openf):
                if n not in visited:
                    visited.add(n)
                    distances[n] = distances[vert] + 1
                    Q.append(n)


def count_visited(source, openf):
    distances[source] = 0
    bfs(source, openf)
    return len(visited)


favourite_number = read_input()
open_function = lambda x, y: is_open(x, y, favourite_number)
target = (31, 39)
initial = (1, 1)
result = count_visited(initial, open_function)
print(result)
