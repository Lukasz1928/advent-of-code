

def read_input():
    with open('input', 'r') as f:
        return [(int(c[0]), int(c[1])) for c in [l.replace(' ', '').split(',') for l in f]]


def distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def get_closest(x, y, points):
    distances = [distance((x, y), p) for p in points]
    min_dist = min(distances)
    return distances.index(min_dist) if distances.count(min_dist) == 1 else None


coords = read_input()
maxx, maxy = max(x[0] for x in coords), max(x[1] for x in coords)
grid = [[get_closest(x, y, coords) for x in range(maxx + 2)] for y in range(maxy + 2)]

border_coords = (set(grid[0][x] for x in range(maxx + 2)) | set(grid[maxy + 1][x] for x in range(maxx + 2)) |
                 set(grid[y][0] for y in range(maxy + 2)) | set(grid[y][maxx + 1] for y in range(maxy + 2)))

possible_coords = set(range(len(coords)))
counts = {c: 0 for c in possible_coords}
for y in range(maxy + 2):
    for x in range(maxx + 2):
        if grid[y][x] is not None:
            counts[grid[y][x]] += 1

for bc in border_coords - {None}:
    counts[bc] = -1

result = max(counts.values())
print(result)
