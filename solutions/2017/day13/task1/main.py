import re


def read_input():
    ls = {}
    with open('input', 'r') as f:
        for l in f:
            m = re.match('(\\d+): (\\d+)', l)
            ls[int(m.group(1))] = int(m.group(2))
    return ls


def move_scanners(positions, params, directions):
    ids = positions.keys()
    for i in ids:
        r = params[i]
        dir = directions[i]
        pos = positions[i]
        if dir == 1:
            if pos < r - 1:
                positions[i] += 1
            else:
                positions[i] -= 1
                directions[i] = -1
        else:  # dir == -1
            if pos > 0:
                positions[i] -= 1
            else:
                positions[i] += 1
                directions[i] = 1
    return positions, directions


scanners_params = read_input()
scanners_position = {s: 0 for s in scanners_params.keys()}
scanners_direction = {s: 1 for s in scanners_params.keys()}
length = max(scanners_params.keys()) + 1
total_severity = 0
for s in range(length):
    severity = 0
    if s in scanners_params.keys():
        if scanners_position[s] == 0:
            severity = s * scanners_params[s]
    scanners_position, scanners_direction = move_scanners(scanners_position, scanners_params, scanners_direction)
    total_severity += severity
print(total_severity)
