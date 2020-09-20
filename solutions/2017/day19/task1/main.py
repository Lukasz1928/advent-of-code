
def read_input():
    with open('input', 'r') as f:
        m = [" " + x.replace('\n', '') + " " for x in f]
        mlen = max([len(x) for x in m])
        return [" " * mlen] + [x.ljust(mlen) for x in m] + [" " * mlen]


def is_end(maze, pos, start_pos):
    if pos == start_pos:
        return False
    if sum([1 if maze[pos[0] + d[0]][pos[1] + d[1]] == ' ' else 0 for d in {(1, 0), (-1, 0), (0, 1), (0, -1)}]) == 1:
        return True
    return False


def can_go(maze, pos, dir):
    new_pos = (pos[0] + dir[0], pos[1] + dir[1])
    if maze[new_pos[0]][new_pos[1]] == ' ':
        return False
    return True


diagram = read_input()
start_position = (1, diagram[1].index('|'))
position = start_position
direction = (1, 0)

letters = []

while True:
    if can_go(diagram, position, direction):
        position = (position[0] + direction[0], position[1] + direction[1])
        if diagram[position[0]][position[1]].isupper():
            letters.append(diagram[position[0]][position[1]])
    else:
        for d in ({(1, 0), (-1, 0), (0, 1), (0, -1)} - {direction, (-direction[0], -direction[1])}):
            if can_go(diagram, position, d):
                direction = d
                position = (position[0] + direction[0], position[1] + direction[1])
                if diagram[position[0]][position[1]].isupper():
                    letters.append(diagram[position[0]][position[1]])
                break
        else:
            break

result = "".join(letters)
print(result)
