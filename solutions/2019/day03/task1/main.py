from collections import defaultdict

lines = [x for x in open('input', 'r')]
counter = defaultdict(set)
crossings = set()
for num, line in enumerate(lines):
    x, y = 0, 0
    for move in line.split(','):
        d = move[0]
        c = int(move[1:])
        if d == 'U':
            for i in range(c):
                y += 1
                counter[(x, y)].add(num)
                if len(counter[(x, y)]) >= 2:
                    crossings.add((x, y))
        elif d == 'D':
            for i in range(c):
                y -= 1
                counter[(x, y)].add(num)
                if len(counter[(x, y)]) >= 2:
                    crossings.add((x, y))
        elif d == 'L':
            for i in range(c):
                x -= 1
                counter[(x, y)].add(num)
                if len(counter[(x, y)]) >= 2:
                    crossings.add((x, y))
        else:
            for i in range(c):
                x += 1
                counter[(x, y)].add(num)
                if len(counter[(x, y)]) >= 2:
                    crossings.add((x, y))
m = min(crossings, key=lambda x: abs(x[0]) + abs(x[1]))
print(abs(m[0]) + abs(m[1]))
