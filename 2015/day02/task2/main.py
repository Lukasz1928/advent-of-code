data = [x.split('x') for x in open('input', 'r').read().split('\n')]
total = 0
for d in [tuple(sorted((int(x[0]), int(x[1]), int(x[2])))) for x in data]:
    total += 2 * d[0] + 2 * d[1] + d[0] * d[1] * d[2]
print(total)
