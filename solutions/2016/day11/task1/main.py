import re
from collections import deque
from copy import deepcopy


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


def bfs(initial):
    Q = deque()
    Q.append(initial)
    visited = {initial.hash()}
    parents = {initial.hash(): None}
    while len(Q) > 0:
        v = Q.popleft()
        if v.is_goal():
            return parents, v.hash()
        for move in generate_possible_moves(v.floors, v.elevator, True):
            ngh = v.move(move, True)
            h = ngh.hash()
            if h not in visited:
                visited.add(h)
                parents[h] = v.hash()
                Q.append(ngh)
        for move in generate_possible_moves(v.floors, v.elevator, False):
            ngh = v.move(move, False)
            h = ngh.hash()
            if h not in visited:
                visited.add(h)
                parents[h] = v.hash()
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
elevator_level = 0
parents, v = bfs(Vertex(floors, 0))
l = 0
c = v
while c is not None:
    c = parents[c]
    l += 1
result = l - 1
print(result)
