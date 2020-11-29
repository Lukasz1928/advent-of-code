import re
import z3


def read_input():
    with open('input', 'r') as f:
        lines = f.read().splitlines(False)
    bs = []
    for l in lines:
        m = re.match(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', l)
        bot = (int(m.group(1)), int(m.group(2)), int(m.group(3))), int(m.group(4))
        bs.append(bot)
    return bs


def z3_abs(val):
    return z3.If(val >= 0, val, -val)


bots = read_input()

opt = z3.Optimize()

# variables to find
x, y, z = z3.Int('x'), z3.Int('y'), z3.Int('z')

# variables describing if (x, y, z) is in range of a certain bot
ranges = [z3.Int(f'r{idx}') for idx in range(len(bots))]
for ib, b in enumerate(bots):
    cond = z3.If(z3_abs(x - b[0][0]) + z3_abs(y - b[0][1]) + z3_abs(z - b[0][2]) <= b[1], 1, 0)
    opt.add(ranges[ib] == cond)

# number of bots, which cover the (x, y, z) point
in_range_count = z3.Int('sum')
opt.add(in_range_count == sum(ranges))

# distance between (x, y, z) and (0, 0, 0)
origin_distance = z3.Int('origin_distance')
opt.add(origin_distance == z3_abs(x) + z3_abs(y) + z3_abs(z))

max_range_sum = opt.maximize(in_range_count)
min_origin_dist = opt.minimize(origin_distance)
opt.check()

location = opt.model()[x].as_long(), opt.model()[y].as_long(), opt.model()[z].as_long()
result = sum(int(c) for c in location)
print(result)
