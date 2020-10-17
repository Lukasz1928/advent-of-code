

def read_input():
    with open('input', 'r') as f:
        return int(f.read().strip())


def cell_value(x, y, grid_number):
    return (((x + 10) * y + grid_number) * (x + 10) // 100) % 10 - 5


def calculate_partial_sums(g):
    sums = [[0] * len(g[0]) for _ in range(len(g))]
    sums[0][0] = g[0][0]
    for col in range(1, len(g[0])):
        sums[0][col] = sums[0][col - 1] + g[0][col]
    for row in range(1, len(g)):
        for col in range(len(g[0])):
            sums[row][col] = sums[row - 1][col] + sum(g[row][:col + 1])
    return sums


def get_partial_sum(partials, x, y):
    if x < 0 or y < 0:
        return 0
    return partials[x][y]


def square_sum(partials, x, y, s):
    return get_partial_sum(partials, x + s - 1, y + s - 1) - get_partial_sum(partials, x - 1, y + s - 1) - get_partial_sum(partials, x + s - 1, y - 1) + get_partial_sum(partials, x - 1, y - 1)


grid_number = read_input()
grid = [[cell_value(x + 1, y + 1, grid_number) for x in range(300)] for y in range(300)]
partial_sums = calculate_partial_sums(grid)

max_sum = grid[0][0]
max_desc = (0, 0, 1)

for row in range(len(grid)):
    for col in range(len(grid[row])):
        for square_size in range(1, 300 - max(row, col)):
            s = square_sum(partial_sums, col, row, square_size)
            if s > max_sum:
                max_sum = s
                max_desc = (col, row, square_size)

result = '{},{},{}'.format(max_desc[1] + 1, max_desc[0] + 1, max_desc[2])
print(result)
