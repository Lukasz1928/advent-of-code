import re


def read_input():
    with open('input', 'r') as f:
        lines = f.read().splitlines(False)
    bs = []
    for l in lines:
        m = re.match(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', l)
        bot = (int(m.group(1)), int(m.group(2)), int(m.group(3))), int(m.group(4))
        bs.append(bot)
    return bs


def distance(p, q):
    return sum(abs(p[i] - q[i]) for i in range(len(p)))


bots = read_input()


