
with open('input', 'r') as f:
	data = [int(line) for line in f]
data_len = len(data)

idx = 0
count = 0
while True:
	if idx >= data_len or idx < 0:
		break
	new_idx = idx + data[idx]
	data[idx] += 1
	idx = new_idx
	count += 1
print(count)