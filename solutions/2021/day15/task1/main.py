import math
from collections import defaultdict
from queue import PriorityQueue


def read_input():
    with open('input', 'r') as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]


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
lowest_risk = dijkstra(danger_levels)
print(lowest_risk)
