import math

def sum_adjacent(arr, loc):
	return sum([sum(a[loc[1] - 1:loc[1] + 2]) for a in arr[loc[0] - 1:loc[0] + 2]]) - arr[loc[0]][loc[1]]

square = int(open('input', 'r').read())

dx, dy = 1, 1
grid_centre = math.ceil(math.sqrt(square))
grid_size_upper_bound = 2 * grid_centre + 1
loc = (grid_centre, grid_centre)
grid = [[0] * grid_size_upper_bound for _ in range(grid_size_upper_bound)]

grid[loc[0]][loc[1]] = 1
i = 0
found = False
while not found:
	if i == 0:
		for _ in range(dx):
			loc = (loc[0] + 1, loc[1])
			s = sum_adjacent(grid, loc)
			if s > square:
				found = True
				break
			grid[loc[0]][loc[1]] = s
		dx += 1
	elif i == 1:
		for _ in range(dy):
			loc = (loc[0], loc[1] + 1)
			s = sum_adjacent(grid, loc)
			if s > square:
				found = True
				break
			grid[loc[0]][loc[1]] = s
		dy += 1
	elif i == 2:
		for _ in range(dx):
			loc = (loc[0] - 1, loc[1])
			s = sum_adjacent(grid, loc)
			if s > square:
				found = True
				break
			grid[loc[0]][loc[1]] = s
		dx += 1
	else:
		for _ in range(dy):
			loc = (loc[0], loc[1] - 1)
			s = sum_adjacent(grid, loc)
			if s > square:
				found = True
				break
			grid[loc[0]][loc[1]] = s
		dy += 1
	i = (i + 1) % 4

result = s
print(s)
		