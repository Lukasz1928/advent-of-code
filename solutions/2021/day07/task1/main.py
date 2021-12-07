from statistics import median


def read_input():
    with open('input', 'r') as f:
        return [int(x) for x in f.read().split(',')]


def cost(positions, target):
    return sum(abs(p - target) for p in positions)


pos = read_input()
med = median(pos)
if int(med) == med:
    result = cost(pos, int(med))
else:
    c1 = cost(pos, int(med))
    c2 = cost(pos, int(med) + 1)
    result = int(med) if cost(pos, int(med)) else int(med) + 1
print(result)
