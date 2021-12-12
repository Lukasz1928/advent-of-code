from collections import defaultdict, deque


def read_input():
    nghs = defaultdict(lambda: [])
    with open('input', 'r') as f:
        for line in f.readlines():
            l, r = line.strip().split('-')
            nghs[l].append(r)
            nghs[r].append(l)
    return dict(nghs)


neighbors = read_input()
nodes = deque([('start', ('start',))])
paths = {k: [] for k in neighbors.keys()}
while nodes:
    current, current_path = nodes.popleft()
    paths[current].append(current_path)
    if current == 'end':
        continue
    for ngh in neighbors[current]:
        if ngh.upper() == ngh or ngh not in current_path:
            nodes.append((ngh, current_path + (ngh,)))
print(len(paths['end']))
