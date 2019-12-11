current = (0, 0)
visited = {current}


def move(pos, dir):
    if dir == '^':
        return pos[0], pos[1] + 1
    if dir == '>':
        return pos[0] + 1, pos[1]
    if dir == 'v':
        return pos[0], pos[1] - 1
    if dir == '<':
        return pos[0] - 1, pos[1]


for s in open('input', 'r').read():
    current = move(current, s)
    visited.add(current)
print(len(visited))
