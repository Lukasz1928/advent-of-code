from collections import defaultdict, deque


def read_input():
    nghs = defaultdict(list)
    with open('input', 'r') as f:
        for line in f.readlines():
            l, r = line.strip().split('-')
            nghs[l].append(r)
            nghs[r].append(l)
    return dict(nghs)


neighbors = read_input()
nodes = deque([('start', ('start',), {})])
paths = {k: [] for k in neighbors.keys()}
while nodes:
    current, current_path, cnts = nodes.popleft()
    paths[current].append(current_path)
    if current == 'end':
        continue
    can_revisit = not cnts or max(v for v in cnts.values()) < 2
    for ngh in neighbors[current]:
        if ngh.upper() == ngh:
            nodes.append((ngh, current_path + (ngh,), cnts))
        elif ngh != 'start' and ((cnt := cnts.get(ngh, 0)) == 0 or (can_revisit and cnt == 1)):
            new_cnt = {k: v for k, v in cnts.items()}
            new_cnt[ngh] = cnt + 1
            nodes.append((ngh, current_path + (ngh,), new_cnt))
print(len(paths['end']))
