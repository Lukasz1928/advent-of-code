import re

sum = 0
with open('input', 'r') as f:
	for line in f:
		numbers = [int(x) for x in line.split()]
		for i in range(len(numbers)):
			for j in range(i):
				if numbers[i] % numbers[j] == 0:
					sum += numbers[i] // numbers[j]
				elif numbers[j] % numbers[i] == 0:
					sum += numbers[j] // numbers[i]
print(sum)
		