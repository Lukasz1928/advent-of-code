import numpy as np

with open('input', 'r') as f:
	config = [int(b) for b in f.read().split()]
	banks = len(config)

configs = set([tuple(config)])
cycles_count = 0

while True:
	selected_bank = np.argmax(config)
	blocks = config[selected_bank]
	idx = (selected_bank + 1) % banks
	config[selected_bank] = 0
	while blocks > 0:
		config[idx] += 1
		blocks -= 1
		idx = (idx + 1) % banks
	cycles_count += 1
	if tuple(config) in configs:
		break
	else:
		configs.add(tuple(config))
print(cycles_count)