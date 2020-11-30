import math
from collections import deque


def read_input():
    with open('input', 'r') as f:
        lines = [l.strip() for l in f]
    return lines


class Node:
    def __init__(self, location, neighbors, content, dmg=3):
        self.location = location
        self.neighbors = neighbors
        self.content = content
        self.hp = 200
        self.dmg = dmg

    @staticmethod
    def enemy_type(unit_type):
        return 'elf' if unit_type == 'goblin' else 'goblin'

    def _find_all_targets(self, graph):
        return [n.location for n in graph.nodes.values()
                if n.content == Node.enemy_type(self.content)]

    def _is_in_range_of_target(self, graph):
        return any([graph[n].content == Node.enemy_type(self.content) for n in self.neighbors])

    def _find_all_open_squares_in_range_of_targets(self, graph, targets):
        squares = set()
        for t in targets:
            nghs = graph[t].neighbors
            for n in nghs:
                if graph[n].content == 'empty':
                    squares.add(n)
        return squares

    def _find_nodes_with_smallest_distance(self, possible_targets):
        distances = graph.distance_between(self.location, possible_targets)
        if len(distances) == 0:
            return dict()
        min_dist = min(distances.values())
        return {t: d for t, d in distances.items() if d == min_dist and d < math.inf}

    def find_move_target(self, graph):
        if self._is_in_range_of_target(graph):
            return None
        all_targets = self._find_all_targets(graph)
        possible_move_targets = self._find_all_open_squares_in_range_of_targets(graph, all_targets)
        closest_targets = self._find_nodes_with_smallest_distance(possible_move_targets)
        if len(closest_targets) == 0:
            return None
        target = min([t for t in closest_targets])
        return target

    def find_attack_target(self, graph):
        possible_targets = [n for n in self.neighbors if graph[n].content == Node.enemy_type(self.content)]
        if not possible_targets:
            return None
        min_target_hp = min([graph[p].hp for p in possible_targets])
        targets_with_min_hp = [p for p in possible_targets if graph[p].hp == min_target_hp]
        return min(targets_with_min_hp)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            r = self.content
            self.content = 'empty'
            return 1, r
        return 0, None


class Graph:
    def __init__(self, raw_input, elves_attack):
        self.size = len(raw_input), len(raw_input[0])
        self.nodes = {}
        for row_id, row in enumerate(raw_input[1:-1], 1):
            for col_id, cell in enumerate(row[1:-1], 1):
                if cell != '#':
                    if cell == '.':
                        n = Node((row_id, col_id), [], 'empty')
                    elif cell == 'E':
                        n = Node((row_id, col_id), [], 'elf', elves_attack)
                    else:
                        n = Node((row_id, col_id), [], 'goblin')
                    if raw_input[row_id - 1][col_id] != '#':
                        n.neighbors.append((row_id - 1, col_id))
                    if raw_input[row_id + 1][col_id] != '#':
                        n.neighbors.append((row_id + 1, col_id))
                    if raw_input[row_id][col_id - 1] != '#':
                        n.neighbors.append((row_id, col_id - 1))
                    if raw_input[row_id][col_id + 1] != '#':
                        n.neighbors.append((row_id, col_id + 1))
                    self.nodes[(row_id, col_id)] = n

    def __getitem__(self, item):
        return self.nodes[item]

    def __str__(self):
        i = [['#'] * self.size[1] for _ in range(self.size[0])]
        for n in self.nodes:
            if self[n].content == 'empty':
                i[n[0]][n[1]] = '.'
            elif self[n].content == 'elf':
                i[n[0]][n[1]] = 'E'
            elif self[n].content == 'goblin':
                i[n[0]][n[1]] = 'G'
        return '\n'.join([''.join(x) for x in i])

    def distance_between(self, start, ends):
        Q = deque()
        visited = {start}
        distances = {start: 0}
        Q.append(start)
        while Q:
            node = Q.popleft()
            for ngh in self.nodes[node].neighbors:
                if ngh not in visited and self.nodes[ngh].content == 'empty':
                    visited.add(ngh)
                    distances[ngh] = distances[node] + 1
                    Q.append(ngh)
        return {e: distances[e] if e in visited else math.inf for e in ends}

    def _move_unit(self, start, end):
        self[start].content, self[end].content = self[end].content, self[start].content
        self[start].hp, self[end].hp = self[end].hp, self[start].hp
        self[start].dmg, self[end].dmg = self[end].dmg, self[start].dmg

    def step(self):
        players_order = list(sorted([p for p in self.nodes.keys() if self[p].content in {'elf', 'goblin'}]))
        players = [self[p] for p in players_order]
        for player in players:
            if player.content == 'empty':
                continue
            if player.content == 'elf' and not [n for n in self.nodes.values() if n.content == 'goblin']:
                return 1
            if player.content == 'goblin' and not [n for n in self.nodes.values() if n.content == 'elf']:
                return 2

            # move phase
            player_target = player.find_move_target(self)
            if player_target is not None:
                tmp = player.content
                player.content = 'empty'
                distances = self.distance_between(player_target, [n for n in player.neighbors])
                player.content = tmp
                min_dist = min(distances.values())
                move = min([k for k, v in distances.items() if v == min_dist])
                self._move_unit(player.location, move)
                player = self[move]

            # attack phase
            target = player.find_attack_target(graph)
            if target is not None:
                ret = self[target].take_damage(player.dmg)
                if ret == (1, 'elf'):
                    return -1
        return 0


image_graph = read_input()

attack = 4
while True:
    graph = Graph(image_graph, attack)
    round_count = 0
    while True:
        res = graph.step()
        if res != 0:
            break
        round_count += 1
    if res > 0:
        break
    attack += 1

remaining_hp = sum(graph[n].hp for n in graph.nodes if graph[n].content in {'elf', 'goblin'})

result = round_count * remaining_hp
print(result)
