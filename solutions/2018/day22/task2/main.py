import re
import networkx as nx
import numpy as np


def read_input():
    with open('input', 'r') as f:
        lines = f.read().splitlines(False)
    d = re.match(r'depth: (\d+)', lines[0]).group(1)
    targetx, targety = re.match(r'target: (\d+),(\d+)', lines[1]).groups()
    return int(d), (int(targetx), int(targety))


def fill_system(size, target_location, depth):
    geologic_index = np.zeros((size[0] + 1, size[1] + 1), dtype=np.int)
    geologic_index[0, 0] = 0
    for i in range(1, size[0] + 1):
        geologic_index[i, 0] = (i * 16807) % 20183
    for j in range(1, size[1] + 1):
        geologic_index[0, j] = (j * 48271) % 20183
    for i in range(1, size[0] + 1):
        for j in range(1, size[1] + 1):
            geologic_index[i, j] = ((geologic_index[i - 1, j] + depth) * (geologic_index[i, j - 1] + depth)) % 20183
    geologic_index[target_location[0], target_location[1]] = 0
    erosion_level = np.vectorize(lambda x: (x + depth) % 20183)(geologic_index)
    system = np.vectorize(lambda x: x % 3)(erosion_level)
    return system


region_requirements = [{'C', 'T'}, {'C', 'N'}, {'T', 'N'}]


def neighbours(system, loc, size, eq):
    nghs = []
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_loc = (loc[0] + d[0], loc[1] + d[1])
        if 0 <= new_loc[0] < size[0] and 0 <= new_loc[1] < size[1] and eq in region_requirements[system[new_loc[0]][new_loc[1]]]:
            nghs.append((new_loc, eq, 1))
    if eq == 'C':
        nghs.extend([x for x in [(loc, 'T', 7), (loc, 'N', 7)] if x[1] in region_requirements[system[loc[0]][loc[1]]]])
    elif eq == 'T':
        nghs.extend([x for x in [(loc, 'C', 7), (loc, 'N', 7)] if x[1] in region_requirements[system[loc[0]][loc[1]]]])
    else:
        nghs.extend([x for x in [(loc, 'C', 7), (loc, 'T', 7)] if x[1] in region_requirements[system[loc[0]][loc[1]]]])
    return nghs


def build_graph(system, size):
    g = nx.DiGraph()
    for x in range(size[0]):
        for y in range(size[1]):
            for eq in ['T', 'C', 'N']:
                if eq in region_requirements[system[x][y]]:
                    nghs = neighbours(system, (x, y), size, eq)
                    for ngh in nghs:
                        g.add_edge(((x, y), eq), (ngh[0], ngh[1]), weight=ngh[2])
    return g


d, target = read_input()
system_size = target[0] + 100, target[1] + 100
system = fill_system(system_size, target, d)

graph = build_graph(system, system_size)
result = nx.algorithms.shortest_paths.dijkstra_path_length(graph, ((0, 0), 'T'), (target, 'T'))
print(result)
