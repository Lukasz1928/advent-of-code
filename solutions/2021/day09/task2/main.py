from collections import deque


def read_input():
    with open('input', 'r') as f:
        return [[int(h) for h in line.strip()] for line in f.readlines()]


def add_border(data):
    width = len(data[0])
    return [[9] * (width + 2)] + [[9, *line, 9] for line in data] + [[9] * (width + 2)]


def get_low_points(data):
    lows = set()
    for row_idx in range(1, len(data) - 1):
        for col_idx in range(1, len(data[row_idx]) - 1):
            if data[row_idx][col_idx] < min(data[row_idx + i][col_idx + j]
                                            for (i, j) in {(0, 1), (0, -1), (1, 0), (-1, 0)}):
                lows.add((row_idx, col_idx))
    return lows


def find_basin_size(low, data):
    points = deque([low])
    visited = set()
    size = 0
    while points:
        current = points.pop()
        if current in visited:
            continue
        size += 1
        visited.add(current)
        for (i, j) in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
            ngh = (current[0] + i, current[1] + j)
            if 9 > data[ngh[0]][ngh[1]] > data[current[0]][current[1]]:
                points.append(ngh)
    return size


raw_input = read_input()
bordered = add_border(raw_input)
lows = get_low_points(bordered)
sizes = [find_basin_size(low, bordered) for low in lows]
sorted_sizes = sorted(sizes, reverse=True)
result = sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]
print(result)
