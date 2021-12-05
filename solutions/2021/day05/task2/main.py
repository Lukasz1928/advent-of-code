import re
from collections import Counter


def read_input():
    with open('input', 'r') as f:
        _lines = []
        for line in f.readlines():
            m = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line.strip())
            _lines.append(((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))))
    return _lines


def generate_covered_points(p, q):
    dx = int(_dx / abs(_dx)) if (_dx := q[0] - p[0]) != 0 else 0
    dy = int(_dy / abs(_dy)) if (_dy := q[1] - p[1]) != 0 else 0
    point = p
    while point != q:
        yield point
        point = (point[0] + dx, point[1] + dy)
    yield q


lines = read_input()
covered_points = [pt for line in lines for pt in generate_covered_points(*line)]
point_count = Counter(covered_points)
overlapping_points = [pt for pt, cnt in point_count.items() if cnt > 1]
result = len(overlapping_points)
print(result)
