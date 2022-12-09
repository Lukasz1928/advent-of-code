def read_input() -> list[list[int]]:
    with open('input', 'r') as f:
        return [[int(tree) for tree in line.strip()] for line in f]


data = read_input()
visible = 0
changes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for row_idx, row in enumerate(data):
    for col_idx, tree in enumerate(row):
        for change in changes:
            is_visible = True
            i = 1
            while 0 <= (r := row_idx + change[0] * i) < len(data) and 0 <= (c := col_idx + change[1] * i) < len(data[0]):
                if data[r][c] >= tree:
                    is_visible = False
                    break
                i += 1
            if is_visible:
                visible += 1
                break
print(visible)
