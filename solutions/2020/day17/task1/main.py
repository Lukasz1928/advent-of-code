import numpy as np


def read_input():
    with open('input', 'r') as f:
        return [[1 - (elem == '.') for elem in x.strip()] for x in f.readlines()]


def step(arr):
    new_arr = np.zeros(arr.shape)
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            for z in range(arr.shape[2]):
                active_nghs = np.sum(arr[max(0, x - 1):min(x + 2, arr.shape[0]),
                                     max(0, y - 1):min(y + 2, arr.shape[1]),
                                     max(0, z - 1):min(z + 2, arr.shape[2])]) - arr[x, y, z]
                if arr[x, y, z] == 1:
                    new_arr[x, y, z] = 1 if active_nghs in {2, 3} else 0
                else:
                    new_arr[x, y, z] = 1 if active_nghs == 3 else 0
    return new_arr


initial_state = read_input()
state_2d = np.asarray(initial_state)
state = np.zeros((len(initial_state), len(initial_state), len(initial_state)))
state[:, :, 1] = state_2d
for _ in range(6):
    new_state = np.zeros((state.shape[0] + 2, state.shape[1] + 2, state.shape[2] + 2))
    new_state[1:-1, 1:-1, 1:-1] = state
    state = step(new_state)
result = int(np.sum(state))
print(result)
