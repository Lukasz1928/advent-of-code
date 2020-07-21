
def are_anagrams(w1, w2):
	return sorted(w1) == sorted(w2)

def is_valid(words):
	for i in range(len(words)):
		for j in range(i):
			if are_anagrams(words[i], words[j]):
				return False
	return True

valid_count = 0
with open('input', 'r') as f:
	for line in f:
		words = line.split()
		if is_valid(words):
			valid_count += 1
print(valid_count)
