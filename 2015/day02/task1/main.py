total = 0
with open('input', 'r') as f:
	for line in f:
		dims = [int(d) for d in line.split('x')]
		sides = [dims[0] * dims[1], dims[0] * dims[2], dims[1] * dims[2]]
		total += 2 * sum(sides) + min(sides)
print(total)