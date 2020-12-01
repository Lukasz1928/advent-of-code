

def read_input():
    with open('input', 'r') as f:
        lines = [l.strip() for l in f]
    return lines


class Graph:
    def __init__(self, ranges, source_loc):
        self.nodes = {}
        self.image = None
        self.source_location = source_loc
        self._make_image(ranges, source_loc)
        self._make_graph(ranges)

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
        self.minx = minx - 1

    def _make_graph(self, ranges):
        minx, maxx = min(x[0][0] for x in ranges), max(x[0][1] for x in ranges)
        miny, maxy = 0, max(x[1][1] for x in ranges)
        print(minx, maxx)
        print(miny, maxy)
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                n = Node('dry', {}, (x, y))
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
                            self.nodes[t].neighbors = {direction: coords for direction, coords in self.nodes[t].neighbors.items() if coords != (x, y)}
                        except (ValueError, KeyError):
                            pass

    def __str__(self):
        return '\n'.join([''.join(x) for x in self.image])


    def add_water(self):
        self.nodes[self.source_location].add_water()


class Node:
    def __init__(self, wetness, nghs, location):
        self.wetness = wetness
        self.neighbors = nghs
        self.location = location

    def add_water(self):


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
# print(graph)
