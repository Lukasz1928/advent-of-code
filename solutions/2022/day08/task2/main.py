def read_input() -> list[list[int]]:
    with open('input', 'r') as f:
        return [[int(tree) for tree in line.strip()] for line in f]


data = read_input()
visible = 0
changes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_score = 0
for row_idx, row in enumerate(data):
    for col_idx, tree in enumerate(row):
        score = 1
        for change in changes:
            dir_score = 0
            i = 1
            while 0 <= (r := row_idx + change[0] * i) < len(data) and 0 <= (c := col_idx + change[1] * i) < len(data[0]):
                dir_score += 1
                if data[r][c] >= tree:
                    break
                i += 1
            score *= dir_score
        max_score = max(max_score, score)
print(max_score)
