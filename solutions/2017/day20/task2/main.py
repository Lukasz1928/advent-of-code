import re
from collections import defaultdict
from math import sqrt


def read_input():
    r = []
    with open('input', 'r') as f:
        for l in f:
            pattern = "p=<(-?\\d+),(-?\\d+),(-?\\d+)>, v=<(-?\\d+),(-?\\d+),(-?\\d+)>, a=<(-?\\d+),(-?\\d+),(-?\\d+)>"
            m = re.match(pattern, l.strip())
            r.append(((int(m.group(1)), int(m.group(2)), int(m.group(3))),
                      (int(m.group(4)), int(m.group(5)), int(m.group(6))),
                      (int(m.group(7)), int(m.group(8)), int(m.group(9)))))
    return r


def solve_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return 'all'
            else:
                return 'none'
        else:
            return {-c / b}
    else:
        d = b * b - 4 * a * c
        if d < 0:
            return 'none'
        if d == 0:
            return {-b / (2 * a)}
        return {x for x in {(-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)} if x > 0}


def calculate_collision_time(p1, p2):
    s1 = solve_equation(p1[2][0] / 2.0 - p2[2][0] / 2.0, p1[1][0] + p1[2][0] / 2.0 - p2[1][0] - p2[2][0] / 2.0, p1[0][0] - p2[0][0])
    s2 = solve_equation(p1[2][1] / 2.0 - p2[2][1] / 2.0, p1[1][1] + p1[2][1] / 2.0 - p2[1][1] - p2[2][1] / 2.0, p1[0][1] - p2[0][1])
    s3 = solve_equation(p1[2][2] / 2.0 - p2[2][2] / 2.0, p1[1][2] + p1[2][2] / 2.0 - p2[1][2] - p2[2][2] / 2.0, p1[0][2] - p2[0][2])
    if s1 == 'none' or s2 == 'none' or s3 == 'none':
        return {}
    if s1 == 'all':
        if s2 == 'all':
            if s3 == 'all':  # s1=all, s2=all, s3=all
                return {0}
            else:  # s1=all, s2=all, s3={p,q}
                return s3
        else:
            if s3 == 'all':  # s1=all, s2={p,q}, s3=all
                return s2
            else:  # s1=all, s2={p,q}, s3={r, s}
                return s2.intersection(s3)
    else:
        if s2 == 'all':
            if s3 == 'all':  # s1={p, q}, s2=all, s3=all
                return s1
            else:  # s1={p, q}, s2=all, s3={r, s}
                return s1.intersection(s3)
        else:
            if s3 == 'all':  # s1={p, q}, s2={r, s}, s3=all
                return s1.intersection(s2)
            else:  # s1={p, q}, s2={r, s}, s3={t, u}
                return s1.intersection(s2).intersection(s3)


def find_possible_collisions(particles):
    collisions = defaultdict(lambda: [])
    for i, p1 in enumerate(particles):
        for j, p2 in enumerate(particles):
            t = calculate_collision_time(p1, p2)
            for _t in t:
                if 0 < _t == int(_t):
                    collisions[int(_t)].append((i, j))
    return dict(collisions)


p = read_input()
pc = find_possible_collisions(p)
removed = set()
for t in list(sorted(pc.keys())):
    collisions = [x for x in pc[t] if x[0] not in removed and x[1] not in removed]
    for c in collisions:
        removed.add(c[0])
        removed.add(c[1])

result = len(p) - len(removed)
print(result)
