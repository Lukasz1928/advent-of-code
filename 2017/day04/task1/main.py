valid_count = 0
with open('input', 'r') as f:
	for line in f:
		words = line.split()
		if len(words) == len(set(words)):
			valid_count += 1
print(valid_count)
