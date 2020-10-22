

def read_input():
    with open('input', 'r') as f:
        return [[c for c in l.strip()] for l in f]


def neighbours(x, y, xlim, ylim):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx != 0 or dy != 0) and 0 <= x + dx < xlim and 0 <= y + dy < ylim:
                yield x + dx, y + dy


def step(a):
    size = len(a), len(a[0])
    new = [['.'] * size[1] for _ in range(size[0])]
    for row in range(size[0]):
        for col in range(size[1]):
            nghs = [a[y][x] for x, y in neighbours(col, row, size[1], size[0])]
            current = a[row][col]
            if current == '.':
                new[row][col] = '|' if nghs.count('|') >= 3 else a[row][col]
            elif current == '|':
                new[row][col] = '#' if nghs.count('#') >= 3 else a[row][col]
            else:  # current == '#'
                new[row][col] = '#' if nghs.count('#') >= 1 and nghs.count('|') >= 1 else '.'
    return new


def value(a):
    flat_a = [a[y][x] for y in range(len(a)) for x in range(len(a[y]))]
    return flat_a.count('|') * flat_a.count('#')


def to_hashable(a):
    return tuple([tuple(x) for x in a])


area = read_input()

seen = {to_hashable(area)}
previous = [area]
step_no = 0
while True:
    step_no += 1
    area = step(area)
    h = to_hashable(area)
    if h in seen:
        break
    seen.add(h)
    previous.append(h)

initial_steps = previous.index(h)
period_length = step_no - initial_steps
iterations_from_first_repeated = (1000000000 - initial_steps) % period_length
for _ in range(iterations_from_first_repeated):
    area = step(area)

total_value = value(area)
print(total_value)
