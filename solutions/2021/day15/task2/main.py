import math
from collections import defaultdict
from queue import PriorityQueue
import numpy as np


def read_input():
    with open('input', 'r') as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]


def generate_full_cave(original_levels):
    x = np.asarray(original_levels, dtype=int)
    full = np.vstack([np.hstack([np.vectorize(lambda e: e if e < 10 else e - 9)(x + r + c) for r in range(5)])
                      for c in range(5)])
    return full.tolist()


def nghs(x, y, size):
    for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
        if 0 <= x + dx < size and 0 <= y + dy < size:
            yield x + dx, y + dy


def dijkstra(levels):
    size = len(levels)
    visited = set()
    distances = defaultdict(lambda: math.inf, {(0, 0): 0})
    q = PriorityQueue()
    q.put((0, (0, 0)))
    while not q.empty():
        dist, current = q.get()
        visited.add(current)
        for ngh in nghs(*current, size):
            if ngh not in visited:
                if distances[ngh] > (new_cost := distances[current] + levels[ngh[0]][ngh[1]]):
                    q.put((new_cost, ngh))
                    distances[ngh] = new_cost
    return distances[(size - 1, size - 1)]


danger_levels = read_input()
full_danger_levels = generate_full_cave(danger_levels)
lowest_risk = dijkstra(full_danger_levels)
print(lowest_risk)
