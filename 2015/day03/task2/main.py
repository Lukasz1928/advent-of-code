with open('input', 'r') as f:
	data = f.read()
loc = [(0, 0), (0, 0)]
visited = set([(0, 0)])
i = 0
for dir in data:
	if dir == '^':
		loc[i] = (loc[i][0] + 1, loc[i][1])
	elif dir == 'v':
		loc[i] = (loc[i][0] - 1, loc[i][1])
	elif dir == '>':
		loc[i] = (loc[i][0], loc[i][1] + 1)
	else:
		loc[i] = (loc[i][0], loc[i][1] - 1)
	visited.add(loc[i])
	i = (i + 1) % 2
result = len(visited)
print(result)