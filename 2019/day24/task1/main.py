from copy import deepcopy


def get_neighbours(x, y):
    return [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]


def in_board(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def board2str(board):
    str = ""
    for i in range(5):
        for j in range(5):
            str += board[i][j]
        str += '\n'
    return str


def bugged_neighbours_count(board, x, y):
    nghs = get_neighbours(x, y)
    cnt = 0
    for n in nghs:
        if in_board(*n) and board[n[0]][n[1]] == '#':
            cnt += 1
    return cnt


def next_step(board):
    new_board = deepcopy(board)
    for i in range(5):
        for j in range(5):
            bugged_nghs = bugged_neighbours_count(board, i, j)
            if board[i][j] == '.' and bugged_nghs in {1, 2}:
                new_board[i][j] = '#'
            elif board[i][j] == '#' and bugged_nghs != 1:
                new_board[i][j] = '.'
    return new_board


def biodiversity(board):
    bd = 0
    power = 1
    for i in range(5):
        for j in range(5):
            if board[i][j] == '#':
                bd += power
            power *= 2
    return bd


board = [[x for x in line] for line in open('input', 'r').read().splitlines()]
biodiversities = {biodiversity(board)}
result = None
while True:
    board = next_step(board)
    bd = biodiversity(board)
    if bd in biodiversities:
        result = bd
        break
    biodiversities.add(bd)
print(result)
