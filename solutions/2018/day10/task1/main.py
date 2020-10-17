import re


def read_input():
    points = []
    with open('input', 'r') as f:
        for line in f:
            m = re.match(r'position=<(?P<px>-?\d+),(?P<py>-?\d+)>velocity=<(?P<vx>-?\d+),(?P<vy>-?\d+)>', line.replace(' ', ''))
            points.append(((int(m.group('px')), int(m.group('py'))), (int(m.group('vx')), int(m.group('vy')))))
    return points


def step(points):
    return [((p[0][0] + p[1][0], p[0][1] + p[1][1]), p[1]) for p in points]


def draw_points(pts):
    minx, maxx = min(x[0] for x in pts), max(x[0] for x in pts)
    miny, maxy = min(x[1] for x in pts), max(x[1] for x in pts)
    xlen = maxx - minx + 1
    ylen = maxy - miny + 1
    pts_set = set(pts)
    img = [['#' if (x + minx, y + miny) in pts_set else '.' for x in range(xlen)] for y in range(ylen)]
    img_str = '\n'.join([''.join(row) for row in img])
    print(img_str)


def is_dense(pts):
    miny, maxy = min(x[0][1] for x in pts), max(x[0][1] for x in pts)
    return maxy - miny + 1 < 20  # height selected by trial and error


points = read_input()
while not is_dense(points):
    points = step(points)
draw_points([x[0] for x in points])
