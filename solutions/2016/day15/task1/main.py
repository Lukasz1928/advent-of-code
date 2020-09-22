# note: in input all numbers of positions are prime so by Chinese Remainder Theorem
# there exists a unique solution between 0 and the product of numbers of positions on each disc

import re


def read_input():
    positions = {}
    inits = {}
    with open('input', 'r') as f:
        for line in f:
            match = re.match(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)\.', line.strip())
            disc = int(match.group(1))
            pos = int(match.group(2))
            init = int(match.group(3))
            positions[disc] = pos
            inits[disc] = init
    return positions, inits


def solve_equations(cs):
    x = cs[0][0]
    dif = 1
    for i in range(1, len(cs)):
        mod = cs[i][1]
        dif *= cs[i - 1][1]
        k = 0
        while (x + k * dif) % mod != cs[i][0]:
            k += 1
        x = (x + k * dif)
    return x


positions, initial_positions = read_input()
waits = {k: v - initial_positions[k] for k, v in positions.items()}
coefs = [((waits[i] - i) % positions[i], positions[i]) for i in positions.keys()]
result = solve_equations(coefs)
print(result)
