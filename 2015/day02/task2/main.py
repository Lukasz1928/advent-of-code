import numpy as np

total = 0
with open('input', 'r') as f:
	for line in f:
		dims = [int(d) for d in line.split('x')]
		total += np.product(dims) + 2 * (sum(dims) - max(dims))
print(total)