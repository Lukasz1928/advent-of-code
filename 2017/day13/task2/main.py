import re


def read_input():
    ls = {}
    with open('input', 'r') as f:
        for l in f:
            m = re.match('(\\d+): (\\d+)', l)
            ls[int(m.group(1))] = int(m.group(2)) - 1
    return ls


def position_after(r, time):
    pos_in_period = time % (2 * r)
    if pos_in_period < r:
        return pos_in_period
    else:
        return (2 * r) - pos_in_period


scanners_params = read_input()
length = max(scanners_params.keys()) + 1
delay = 0
while True:
    caught = False
    for s in scanners_params.keys():
        pos = position_after(scanners_params[s], delay + s)
        if pos == 0:
            caught = True
            break
    if not caught:
        break
    delay += 1
print(delay)
