import re


def read_input():
    pts = []
    with open('input', 'r') as f:
        for line in f:
            m = re.match(r'Step (\w) must be finished before step (\w) can begin\.', line)
            pts.append((m.group(1), m.group(2)))
    return pts


def edges_to(node, edges):
    return [x for x in edges if x[1] == node]


def neighbours(node, edges):
    return [x[1] for x in edges if x[0] == node]


def get_ready_nodes(processes, nodes, edges):
    ready = set()
    for n in nodes:
        if n not in processes:
            all_predecessors_processed = True
            for e in edges_to(n, edges):
                if e[0] not in processes:
                    all_predecessors_processed = False
                    break
            if all_predecessors_processed:
                ready.add(n)
    return ready


def traverse(vertices, edges):
    processed = set()
    to_process = set(vertices)
    order = []
    while len(to_process) > 0:
        ready = get_ready_nodes(processed, vertices, edges)
        node = min(ready)
        processed.add(node)
        to_process.remove(node)
        order.append(node)
    return order


order = read_input()
vertices = set(x[0] for x in order) | set(x[1] for x in order)
traversal_order = traverse(vertices, set(order))
result = ''.join(traversal_order)
print(result)
