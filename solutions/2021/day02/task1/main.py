
def read_input():
    with open('input', 'r') as f:
        return [((l := line.split())[0], int(l[1])) for line in f.readlines()]


course = read_input()
changes = [{'forward': (v, 0), 'down': (0, v), 'up': (0, -v)}[i] for i, v in course]
position = (0, 0)
for change in changes:
    position = (position[0] + change[0], position[1] + change[1])
result = position[0] * position[1]
print(result)
