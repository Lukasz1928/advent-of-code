from collections import defaultdict

lines = [x for x in open('input', 'r')]
counter = defaultdict(set)
dist = defaultdict(lambda: {0: -1, 1: -1})
crossings = set()
for num, line in enumerate(lines):
    x, y = 0, 0
    moves = 0
    for move in line.split(','):
        d = move[0]
        c = int(move[1:])
        if d == 'U':
            for i in range(c):
                y += 1
                moves += 1
                counter[(x, y)].add(num)
                dist[(x, y)][num] = moves if moves < dist[(x, y)][num] or dist[(x, y)][num] == -1 else dist[(x, y)][num]
                if len(counter[(x, y)]) >= 2:
                    crossings.add((x, y))
        elif d == 'D':
            for i in range(c):
                y -= 1
                moves += 1
                counter[(x, y)].add(num)
                dist[(x, y)][num] = moves if moves < dist[(x, y)][num] or dist[(x, y)][num] == -1 else dist[(x, y)][num]
                if len(counter[(x, y)]) >= 2:
                    crossings.add((x, y))
        elif d == 'L':
            for i in range(c):
                x -= 1
                moves += 1
                counter[(x, y)].add(num)
                dist[(x, y)][num] = moves if moves < dist[(x, y)][num] or dist[(x, y)][num] == -1 else dist[(x, y)][num]
                if len(counter[(x, y)]) >= 2:
                    crossings.add((x, y))
        else:
            for i in range(c):
                x += 1
                moves += 1
                counter[(x, y)].add(num)
                dist[(x, y)][num] = moves if moves < dist[(x, y)][num] or dist[(x, y)][num] == -1 else dist[(x, y)][num]
                if len(counter[(x, y)]) >= 2:
                    crossings.add((x, y))
m = min([x for x in crossings if dist[x][0] > 0 and dist[x][1] > 0], key=lambda x: dist[x][0] + dist[x][1])
print(dist[m][0] + dist[m][1])