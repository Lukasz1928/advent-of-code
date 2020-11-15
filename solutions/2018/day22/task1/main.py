import re
import numpy as np


def read_input():
    with open('input', 'r') as f:
        lines = f.read().splitlines(False)
    d = re.match(r'depth: (\d+)', lines[0]).group(1)
    targetx, targety = re.match(r'target: (\d+),(\d+)', lines[1]).groups()
    return int(d), (int(targetx), int(targety))


def fill_system(target_location, depth):
    geologic_index = np.zeros((target_location[0] + 1, target_location[1] + 1), dtype=np.int)
    geologic_index[0, 0] = 0
    for i in range(1, target_location[0] + 1):
        geologic_index[i, 0] = (i * 16807) % 20183
    for j in range(1, target_location[1] + 1):
        geologic_index[0, j] = (j * 48271) % 20183
    for i in range(1, target_location[0] + 1):
        for j in range(1, target_location[1] + 1):
            geologic_index[i, j] = ((geologic_index[i - 1, j] + depth) * (geologic_index[i, j - 1] + depth)) % 20183
    geologic_index[target_location[0], target_location[1]] = 0
    erosion_level = np.vectorize(lambda x: (x + depth) % 20183)(geologic_index)
    system = np.vectorize(lambda x: x % 3)(erosion_level)
    return system


d, target = read_input()
system = fill_system(target, d)
risk_sum = np.sum(system)
print(risk_sum)
