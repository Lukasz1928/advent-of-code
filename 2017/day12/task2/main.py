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


def find_programs_in_group(pipes, pid):
    visited = {p: False for p in pipes.keys()}
    to_visit = [pid]
    while len(to_visit) > 0:
        current = to_visit.pop(0)
        if visited[current]:
            continue
        visited[current] = True
        for p in pipes[current]:
            to_visit.append(p)
    return set(p for p, v in visited.items() if v)


def find_number_of_groups(pipes):
    ids = set(pipes.keys())
    groups = 0
    while len(ids) > 0:
        current_id = ids.pop()
        current_group = find_programs_in_group(pipes, current_id)
        ids = ids - (current_group - {current_id})
        groups += 1
    return groups


raw_input = read_input()
data = parse_input(raw_input)
gcount = find_number_of_groups(data)
print(gcount)
