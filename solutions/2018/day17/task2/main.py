# That's an atrocious solution but it somehow works
# I'll probably come back here after some time


def read_input():
    with open('input', 'r') as f:
        lines = [l.strip() for l in f]
    return lines


class Graph:
    def __init__(self, ranges, source_loc):
        self.nodes = {}
        self.wet_nodes = set()

        self.image = None
        self.source_location = source_loc
        self._make_image(ranges, source_loc)
        self._make_graph(ranges)

        self.ranges = ranges

    def _make_image(self, ranges, source_location):
        minx, maxx = min(x[0][0] for x in ranges), max(x[0][1] for x in ranges)
        miny, maxy = 0, max(x[1][1] for x in ranges)
        self.image = [['.'] * (maxx - minx + 3) for _ in range(miny, maxy + 1)]
        for rng in ranges:
            xr, yr = rng
            for x in range(xr[0], xr[1] + 1):
                for y in range(yr[0], yr[1] + 1):
                    self.image[y - miny][x - minx + 1] = '#'
        self.image[source_location[1] - miny][source_location[0] - minx + 1] = '+'
        for node in self.nodes.values():
            if node.wetness == 'water':
                l = node.location
                self.image[l[1]][l[0] - minx + 1] = '~'
            elif node.contained_water:
                l = node.location
                self.image[l[1]][l[0] - minx + 1] = '|'
        self.minx = minx - 1
        self.miny = min(x[1][0] for x in ranges)

    def __getitem__(self, item):
        return self.nodes[item]

    def _make_graph(self, ranges):
        minx, maxx = min(x[0][0] for x in ranges) - 1, max(x[0][1] for x in ranges) + 1
        miny, maxy = 0, max(x[1][1] for x in ranges)
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                n = Node('dry', {}, (x, y), y == maxy, x in {minx, maxx})
                if x != minx:
                    n.neighbors['left'] = (x - 1, y)
                if x != maxx:
                    n.neighbors['right'] = (x + 1, y)
                if y != maxy:
                    n.neighbors['down'] = (x, y + 1)
                if y != miny:
                    n.neighbors['up'] = (x, y - 1)
                self.nodes[(x, y)] = n
        for rng in ranges:
            xr, yr = rng
            for x in range(xr[0], xr[1] + 1):
                for y in range(yr[0], yr[1] + 1):
                    try:
                        self.nodes.pop((x, y))
                    except KeyError:
                        pass
                    for t in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
                        try:
                            self.nodes[t].neighbors = {direction: coords
                                                       for direction, coords in self.nodes[t].neighbors.items()
                                                       if coords != (x, y)}
                        except (ValueError, KeyError):
                            pass
        for node in self.nodes.values():
            node.check_directions_viability(self)

    def __str__(self):
        self._make_image(self.ranges, self.source_location)
        return '\n'.join([''.join(x) for x in self.image])

    def add_water(self):
        n = self.nodes[self.source_location]
        d = 'up'
        while n is not None:
            n, d = n.add_water(self, d)


reversed_direction = {
    'left': 'right',
    'right': 'left',
    'up': 'down',
    'down': 'left'
}


class Node:
    def __init__(self, wetness, nghs, location, final=False, boundary=False):
        self.wetness = wetness
        self.neighbors = nghs
        self.valid = {'up': False,
                      'down': 'down' in self.neighbors,
                      'left': 'left' in self.neighbors,
                      'right': 'right' in self.neighbors}
        self.location = location
        self.final = final
        self.contained_water = False
        self.boundary = boundary

        self.horizontal_direction = 'left'
        self.viable_directions = []
        self.filled_directions = set()
        self.checked = False

    def _has_wall_on_side(self, direction, graph):
        n = self
        while True:
            if n.boundary:
                return False
            if n is not self and 'down' in n.neighbors.keys() and graph[n.neighbors['down']].wetness != 'water':
                return False
            if direction not in n.neighbors.keys():
                return True
            n = graph[n.neighbors[direction]]

    def check_directions_viability(self, graph):
        lw = self._has_wall_on_side('left', graph)
        rw = self._has_wall_on_side('right', graph)
        if (lw and rw) or (not lw and not rw):
            self.viable_directions = [x for x in ['left', 'right'] if x in self.neighbors.keys()]
        elif lw and not rw:
            self.viable_directions = [x for x in ['right'] if x in self.neighbors.keys()]
        elif rw and not lw:
            self.viable_directions = [x for x in ['left'] if x in self.neighbors.keys()]

    def _fill_direction(self, direction, graph):
        n = self
        while True:
            if n.location not in graph.wet_nodes:
                graph.wet_nodes.add(n.location)
            n.wetness = 'wet'
            n.contained_water = True
            if direction not in n.neighbors.keys():
                break
            n = graph[n.neighbors[direction]]

    def add_water(self, graph, came_from):
        if not self.contained_water:
            self.contained_water = True
            if self.location[1] >= graph.miny:
                graph.wet_nodes.add(self.location)
        if self.final:
            return None, None
        if 'down' in self.neighbors.keys() and graph[self.neighbors['down']].wetness != 'water':
            return graph[self.neighbors['down']], 'up'
        if 'down' not in self.neighbors.keys() or graph[self.neighbors['down']].wetness == 'water':
            self.check_directions_viability(graph)
            for x in {'left', 'right'} - set(self.viable_directions):
                self._fill_direction(x, graph)
            # self.checked = True
        if came_from == 'up':
            if len(self.viable_directions) == 0:
                self.wetness = 'water'
                return None, None
            elif len(self.viable_directions) == 1:
                if graph[self.neighbors[self.viable_directions[0]]].wetness == 'water':
                    self.wetness = 'water'
                    return None, None
                if reversed_direction[self.viable_directions[0]] not in self.filled_directions:
                    self._fill_direction(reversed_direction[self.viable_directions[0]], graph)
                return graph[self.neighbors[self.viable_directions[0]]], reversed_direction[self.viable_directions[0]]
            else:  # len(self.viable_direction) == 2
                if self.horizontal_direction in self.neighbors.keys() \
                        and graph[self.neighbors[self.horizontal_direction]].wetness != 'water':
                    n = graph[self.neighbors[self.horizontal_direction]]
                    self.horizontal_direction = reversed_direction[self.horizontal_direction]
                    self.wetness = 'wet'
                    return n, self.horizontal_direction
                rev_dir = reversed_direction[self.horizontal_direction]
                if rev_dir in self.neighbors.keys() and graph[self.neighbors[rev_dir]].wetness != 'water':
                    self.wetness = 'wet'
                    return graph[self.neighbors[
                        reversed_direction[self.horizontal_direction]]], self.horizontal_direction
                self.wetness = 'wet' if self.final else 'water'
                return None, None
        else:  # water came from side
            rev_dir = reversed_direction[came_from]
            if rev_dir in self.neighbors.keys() and graph[self.neighbors[rev_dir]].wetness != 'water':
                return graph[self.neighbors[rev_dir]], came_from
            else:
                self.wetness = 'water' if not self.final else 'wet'
                return None, None


def parse_range(rng):
    if rng.isnumeric():
        return int(rng), int(rng)
    parts = rng.split('..')
    return int(parts[0]), int(parts[1])


def parse_input(lines):
    clay = []
    for line in lines:
        parts = line.split(', ')
        pl, pr = parse_range(parts[0][2:]), parse_range(parts[1][2:])
        clay.append((pl, pr) if parts[0][0] == 'x' else (pr, pl))
    return clay


raw_input = read_input()
clay_ranges = parse_input(raw_input)
source_location = (500, 0)

graph = Graph(clay_ranges, source_location)

wet = len(graph.wet_nodes)
while True:
    for _ in range(3000):
        graph.add_water()
    w = len(graph.wet_nodes)
    if w == wet:
        break
    wet = w

result = len([n for n in graph.nodes.values() if n.wetness == 'water'])
print(result)
