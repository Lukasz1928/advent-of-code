# Absolutely atrocious solution but at least it works
import re
from collections import deque, defaultdict
from copy import deepcopy
from dataclasses import dataclass, field
from queue import PriorityQueue


class Floor:
    def __init__(self, chips, generators):
        self.chips = list(chips)
        self.generators = list(generators)

    def copy(self):
        return Floor(deepcopy(self.chips), deepcopy(self.generators))

    def hash(self):
        return tuple(sorted(self.chips)), tuple(sorted(self.generators))

    def __len__(self):
        return len(self.chips) + len(self.generators)

    def can_be_removed(self, items):
        c = list(self.chips)
        g = list(self.generators)
        for it in items:
            if it[1] == 'generator':
                g.remove(it[0])
            else:
                c.remove(it[0])
        if len(c) == 0:
            return True
        if len(g) == 0:
            return True
        for x in c:
            if x not in g:
                return False
        return True

    def can_be_added(self, items):
        c = list(self.chips)
        g = list(self.generators)
        for it in items:
            if it[1] == 'generator':
                g.append(it[0])
            else:
                c.append(it[0])
        if len(c) == 0:
            return True
        if len(g) == 0:
            return True
        for x in c:
            if x not in g:
                return False
        return True


class Vertex:
    def __init__(self, floors, elevator):
        self.floors = floors
        self.elevator = elevator

    def hash(self):
        return tuple(x.hash() for x in self.floors), self.elevator

    def move(self, items, is_up):
        new_floors = [f.copy() for f in self.floors]
        for it in items:
            if it[1] == 'generator':
                new_floors[self.elevator].generators.remove(it[0])
                new_floors[self.elevator + (1 if is_up else -1)].generators.append(it[0])
            else:
                new_floors[self.elevator].chips.remove(it[0])
                new_floors[self.elevator + (1 if is_up else -1)].chips.append(it[0])
        return Vertex(new_floors, self.elevator + (1 if is_up else -1))

    def is_goal(self):
        return len(self.floors[0]) == len(self.floors[1]) == len(self.floors[2]) == 0


def read_input():
    floors = []
    with open('input', 'r') as f:
        for line in f:
            chips = re.findall(r'(\w+)-compatible microchip', line)
            gens = re.findall(r'(\w+) generator', line)
            floors.append(Floor(chips, gens))
    return floors


@dataclass(order=True)
class QueueItem:
    priority: int
    vertex: Vertex = field(compare=False)


def astar_h(vert):
    return len(vert.floors[2]) * 2 + len(vert.floors[1]) * 4 + len(vert.floors[0]) * 8


def length(parents, v):
    l = 0
    c = v
    while c is not None:
        c = parents[c]
        l += 1
    return l - 1


def astar(initial):
    Q = PriorityQueue()
    Q.put(QueueItem(astar_h(initial), initial))
    queued = {initial.hash()}
    parents = {initial.hash(): None}
    gScore = defaultdict(lambda: 1000000)
    gScore[initial.hash()] = 0
    fScore = defaultdict(lambda: 1000000)
    fScore[initial.hash()] = astar_h(initial)
    while not Q.empty():
        c = Q.get(False)
        current = c.vertex
        current_hash = current.hash()
        queued.remove(current_hash)
        if current.is_goal():
            return parents, current.hash()
        nghs = []
        for move in generate_possible_moves(current.floors, current.elevator, True):
            nghs.append(current.move(move, True))
        for move in generate_possible_moves(current.floors, current.elevator, False):
            nghs.append(current.move(move, False))
        for ngh in nghs:
            gs = gScore[current_hash]
            h = ngh.hash()
            if gs < gScore[h]:
                parents[h] = current_hash
                gScore[h] = gs
                fScore[h] = gScore[h] + astar_h(ngh)
                if h not in queued:
                    queued.add(h)
                    Q.put(QueueItem(astar_h(ngh), ngh))


def bfs(initial, dl, first_up=True):
    Q = deque()
    Q.append(initial)
    visited = {initial.hash()}
    parents = {initial.hash(): None}
    distances = {initial.hash(): 0}
    while len(Q) > 0:
        v = Q.popleft()
        vh = v.hash()
        if distances[vh] > dl:
            return distances
        for move in generate_possible_moves(v.floors, v.elevator, first_up):
            ngh = v.move(move, first_up)
            h = ngh.hash()
            if h not in visited:
                visited.add(h)
                parents[h] = vh
                distances[h] = distances[vh] + 1
                Q.append(ngh)
        for move in generate_possible_moves(v.floors, v.elevator, not first_up):
            ngh = v.move(move, not first_up)
            h = ngh.hash()
            if h not in visited:
                visited.add(h)
                parents[h] = vh
                distances[h] = distances[vh] + 1
                Q.append(ngh)


def generate_possible_moves(floors, current_floor, up):
    if not up:
        res = []
        if current_floor > 0:
            floor_items = [(x, 'microchip') for x in floors[current_floor].chips] + [(x, 'generator') for x in floors[current_floor].generators]
            for i1, it in enumerate(floor_items):
                for it2 in floor_items[i1 + 1:]:
                    if floors[current_floor].can_be_removed([it, it2]) and floors[current_floor - 1].can_be_added([it, it2]):
                        res.append((it, it2))
            for it in floor_items:
                if floors[current_floor].can_be_removed([it]) and floors[current_floor - 1].can_be_added([it]):
                    res.append((it,))

        return res
    res = []
    if current_floor < 3:
        floor_items = [(x, 'microchip') for x in floors[current_floor].chips] + [(x, 'generator') for x in floors[current_floor].generators]
        for i1, it in enumerate(floor_items):
            for it2 in floor_items[i1 + 1:]:
                if floors[current_floor].can_be_removed([it, it2]) and floors[current_floor + 1].can_be_added([it, it2]):
                    res.append((it, it2))
        for it in floor_items:
            if floors[current_floor].can_be_removed([it]) and floors[current_floor + 1].can_be_added([it]):
                res.append((it,))
    return res


floors = read_input()

floors[0].generators.append('elerium')
floors[0].chips.append('elerium')
floors[0].generators.append('dilithium')
floors[0].chips.append('dilithium')


elevator_level = 0
parents, v = astar(Vertex(floors, 0))
upper_bound = length(parents, v)
final_floors = [Floor([], []), Floor([], []), Floor([], []),
                Floor(floors[0].chips + floors[1].chips + floors[2].chips + floors[3].chips,
                      floors[0].generators + floors[1].generators + floors[2].generators + floors[3].generators)]

left = bfs(Vertex(floors, 0), upper_bound//2 + 1, True)
right = bfs(Vertex(final_floors, 3), upper_bound//2 + 1, False)
common = set(left.keys()).intersection(right.keys())
min_dist = upper_bound
for c in common:
    d = left[c] + right[c]
    if d < min_dist:
        min_dist = d
print(min_dist)
