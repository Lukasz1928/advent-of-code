def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


def has_adjacent_part(grid: list[str], row: int, cols: tuple[int, int]) -> bool:
    border = (
        [(row - 1, col) for col in range(cols[0] - 1, cols[1] + 2)] +
        [(row + 1, col) for col in range(cols[0] - 1, cols[1] + 2)] +
        [(row, cols[0] - 1), (row, cols[1] + 1)]
    )
    for item in border:
        if 0 <= item[0] < len(grid) and 0 <= item[1] < len(grid[0]) and grid[item[0]][item[1]] not in '0123456789.':
            return True
    return False


data = read_input()
result = 0
for row_idx, row in enumerate(data):
    col_idx = 0
    last_start = None
    for col_idx, elem in enumerate(row + '.'):
        if elem.isdigit():
            if last_start is None:
                last_start = col_idx
        else:
            if last_start is not None:
                if has_adjacent_part(data, row_idx, (last_start, col_idx - 1)):
                    result += int(row[last_start:col_idx])
                last_start = None
print(result)
