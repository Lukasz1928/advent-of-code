

def read_input():
    with open('input', 'r') as f:
        return int(f.read().strip())


def cell_value(x, y, grid_number):
    return (((x + 10) * y + grid_number) * (x + 10) // 100) % 10 - 5


def square_sum(g, tl):
    square = [r[tl[0]:tl[0] + 3] for r in g[tl[1]:tl[1] + 3]]
    return sum(sum(square, []))


grid_number = read_input()
grid = [[cell_value(x + 1, y + 1, grid_number) for x in range(300)] for y in range(300)]

max_value = square_sum(grid, (0, 0))
max_value_index = (0, 0)
for y in range(300 - 2):
    for x in range(300 - 2):
        v = square_sum(grid, (x, y))
        if v > max_value:
            max_value = v
            max_value_index = (x, y)

result = '{},{}'.format(max_value_index[0] + 1, max_value_index[1] + 1)
print(result)
