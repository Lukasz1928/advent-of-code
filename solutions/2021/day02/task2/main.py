
def read_input():
    with open('input', 'r') as f:
        return [((l := line.split())[0], int(l[1])) for line in f.readlines()]


course = read_input()
position = (0, 0)
aim = 0
for instr, val in course:
    if instr == 'down':
        aim += val
    elif instr == 'up':
        aim -= val
    else:  # forward
        position = (position[0] + val, position[1] + val * aim)
result = position[0] * position[1]
print(result)
