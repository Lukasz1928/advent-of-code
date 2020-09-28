import itertools

import networkx as nx


def read_input():
    with open('input', 'r') as f:
        lines = [l for l in f]
    graph = nx.Graph()
    targets = set()
    initial = None
    for _ri, row in enumerate(lines[1:-1]):
        for _ci, cell in enumerate(row[1:-1]):
            if cell != '#':
                ri = _ri + 1
                ci = _ci + 1
                graph.add_node((ri, ci))
                if cell.isdigit():
                    if cell == '0':
                        initial = (ri, ci)
                    else:
                        targets.add((ri, ci))
                if lines[ri - 1][ci] != '#':
                    graph.add_edge((ri, ci), (ri - 1, ci))
                if lines[ri + 1][ci] != '#':
                    graph.add_edge((ri, ci), (ri + 1, ci))
                if lines[ri][ci - 1] != '#':
                    graph.add_edge((ri, ci), (ri, ci - 1))
                if lines[ri][ci + 1] != '#':
                    graph.add_edge((ri, ci), (ri, ci + 1))
    return graph, targets, initial


def calculate_distances(graph, targets):
    d = {}
    for s in targets:
        p = nx.single_source_shortest_path_length(graph, s)
        d[s] = {k: v for k, v in p.items() if k in targets and k != s}
    return d


def find_shortest_path(initial, targets, ds):
    min_dist = 1000000
    for o in itertools.permutations(list(targets)):
        distance = 0
        current = initial
        for n in o:
            distance += ds[current][n]
            current = n
            if distance >= min_dist:
                break
        if distance < min_dist:
            min_dist = distance
    return min_dist


grid, to_visit, start = read_input()
distances = calculate_distances(grid, to_visit | {start})

result = find_shortest_path(start, to_visit, distances)
print(result)
