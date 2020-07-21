with open('input', 'r') as f:
	data = f.read()
loc = (0, 0)
visited = set([loc])
for dir in data:
	if dir == '^':
		loc = (loc[0] + 1, loc[1])
	elif dir == 'v':
		loc = (loc[0] - 1, loc[1])
	elif dir == '>':
		loc = (loc[0], loc[1] + 1)
	else:
		loc = (loc[0], loc[1] - 1)
	visited.add(loc)
result = len(visited)
print(result)