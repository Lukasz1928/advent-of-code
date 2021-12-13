import re


def read_input():
    with open('input', 'r') as f:
        raw_data = f.read()
    pts_data, folding_data = raw_data.split('\n\n')
    pts = {tuple(int(x) for x in line.split(',')) for line in pts_data.split('\n')}
    folds = [((m := re.match(r'.*?(?P<dir>[xy])=(?P<val>\d+)', line)).group('dir'), int(m.group('val')))
             for line in folding_data.split('\n')]
    return pts, folds


def fold(pt, direction, val):
    if direction == 'x':
        return (2 * val - pt[0], pt[1]) if pt[0] > val else pt
    return (pt[0], 2 * val - pt[1]) if pt[1] > val else pt


def print_points(pts):
    minx, maxx = min(p[0] for p in pts), max(p[0] for p in pts)
    miny, maxy = min(p[1] for p in pts), max(p[1] for p in pts)
    grid = [[' ' for _ in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)]
    for pt in pts:
        grid[pt[1]][pt[0]] = '#'
    img = '\n'.join([''.join(row) for row in grid])
    print(img)


data = read_input()
pts, folds = read_input()

for fld in folds:
    pts = {fold(p, *fld) for p in pts}
print_points(pts)
