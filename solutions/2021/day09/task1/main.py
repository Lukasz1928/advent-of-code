
def read_input():
    with open('input', 'r') as f:
        return [[int(h) for h in line.strip()] for line in f.readlines()]


def add_border(data):
    width = len(data[0])
    return [[9] * (width + 2)] + [[9, *line, 9] for line in data] + [[9] * (width + 2)]


raw_input = read_input()
bordered = add_border(raw_input)
total_danger = 0
for row_idx in range(1, len(bordered) - 1):
    for col_idx in range(1, len(bordered[row_idx]) - 1):
        if bordered[row_idx][col_idx] < min(bordered[row_idx + i][col_idx + j]
                                            for (i, j) in {(0, 1), (0, -1), (1, 0), (-1, 0)}):
            total_danger += bordered[row_idx][col_idx] + 1
print(total_danger)
