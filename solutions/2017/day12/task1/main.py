import re


def read_input():
    with open('input', 'r') as f:
        return [x.strip() for x in f]


def parse_input(i):
    p = {}
    for l in i:
        m = re.match('(\\d+) <-> (.*)', l)
        left = int(m.group(1))
        rights = set(int(x) for x in m.group(2).split(','))
        p[left] = rights
    return p


def find_group_size(pipes, pid):
    visited = {p: False for p in pipes.keys()}
    to_visit = [pid]
    while len(to_visit) > 0:
        current = to_visit.pop(0)
        if visited[current]:
            continue
        visited[current] = True
        for p in pipes[current]:
            to_visit.append(p)
    return sum(visited.values())


raw_input = read_input()
data = parse_input(raw_input)
gsize = find_group_size(data, 0)
print(gsize)
