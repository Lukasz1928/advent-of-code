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


data = read_input()
pts, folds = read_input()

folded_pts = {fold(p, *folds[0]) for p in pts}
result = len(folded_pts)
print(result)
