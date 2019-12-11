current1 = (0, 0)
current2 = (0, 0)
visited = {current1}


def move(pos, dir):
    if dir == '^':
        return pos[0], pos[1] + 1
    if dir == '>':
        return pos[0] + 1, pos[1]
    if dir == 'v':
        return pos[0], pos[1] - 1
    if dir == '<':
        return pos[0] - 1, pos[1]

dirs = open('input', 'r').read()
for s in [dirs[i:i+2] for i in range(0, len(dirs), 2)]:
    current1 = move(current1, s[0])
    visited.add(current1)
    current2 = move(current2, s[1])
    visited.add(current2)
print(len(visited))
