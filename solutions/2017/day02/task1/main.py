import re

sum = 0
with open('input', 'r') as f:
	for line in f:
		numbers = [int(x) for x in line.split()]
		sum += max(numbers) - min(numbers)
print(sum)		