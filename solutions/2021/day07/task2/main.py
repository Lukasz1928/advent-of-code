
def read_input():
    with open('input', 'r') as f:
        return [int(x) for x in f.read().split(',')]


def move_cost(start, end):
    dx = abs(start - end)
    return dx * (dx + 1) // 2


def total_cost(positions, target):
    return sum(move_cost(p, target) for p in positions)


pos = read_input()
min_pos, max_pos = min(pos), max(pos)

min_cost = total_cost(pos, min_pos)
for p in range(min_pos + 1, max_pos + 1):
    if (c := total_cost(pos, p)) < min_cost:
        min_cost = c
print(min_cost)
