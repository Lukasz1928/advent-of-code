square = int(open('input', 'r').read())

dx, dy = 1, 1
loc = (0, 0)

num = 1
i = 0
while True:
	if i == 0:
		loc = (loc[0] + dx, loc[1])
		num += dx
		if num >= square:
			loc = (loc[0] - (num - square), loc[1])
			break
		dx += 1
	elif i == 1:
		loc = (loc[0], loc[1] + dy)
		num += dy
		if num >= square:
			loc = (loc[0], loc[1] - (num - square))
			break
		dy += 1
	elif i == 2:
		loc = (loc[0] - dx, loc[1])
		num += dx
		if num >= square:
			loc = (loc[0] + (num - square), loc[1])
			break
		dx += 1
	else:
		loc = (loc[0], loc[1] - dy)
		num += dy
		if num >= square:
			loc = (loc[0], loc[1] + (num - square))
			break
		dy += 1
	i = (i + 1) % 4

result = abs(loc[0]) + abs(loc[1])
print(result)
		