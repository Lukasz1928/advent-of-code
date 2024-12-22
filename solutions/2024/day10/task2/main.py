def read_input() -> list[list[int]]:
    with open('input', 'r') as f:
        return [[int(x) for x in line.strip()] for line in f]


def is_in_board(board_size: tuple[int, int], location: tuple[int, int]) -> bool:
    return 0 <= location[0] < board_size[0] and 0 <= location[1] < board_size[1]


data = read_input()
size = len(data), len(data[0])

trailheads = {(row_idx, col_idx) for row_idx, row in enumerate(data) for col_idx, elem in enumerate(row) if elem == 0}

neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = 0

for head in trailheads:
    to_visit = [(1, head)]
    score = 0
    while to_visit:
        needed, current_location = to_visit.pop()
        for ngh in neighbours:
            ngh_loc = current_location[0] + ngh[0], current_location[1] + ngh[1]
            if not is_in_board(size, ngh_loc) or data[ngh_loc[0]][ngh_loc[1]] != needed:
                continue
            if needed == 9:
                score += 1
            else:
                to_visit.append((needed + 1, ngh_loc))
    result += score

print(result)
