

def read_input():
    with open('input', 'r') as f:
        return [[x for x in line.strip()] for line in f]


def first_in_direction(board, x, y, dx, dy):
    p = x + dx
    q = y + dy
    while 0 <= p < len(board) and 0 <= q < len(board[p]):
        if board[p][q] != '.':
            return board[p][q]
        p += dx
        q += dy
    return '.'


def occupied_neighbors(board, x, y):
    d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return [first_in_direction(board, x, y, *di) for di in d].count('#')


def step(board):
    new_board = [[x for x in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            occ = occupied_neighbors(board, i, j)
            if board[i][j] == 'L' and occ == 0:
                new_board[i][j] = '#'
            elif board[i][j] == '#' and occ >= 5:
                new_board[i][j] = 'L'
    return new_board


def board_hash(board):
    return ''.join([''.join(x) for x in board])


board = read_input()
prev = board_hash(board)
while True:
    board = step(board)
    h = board_hash(board)
    if h == prev:
        break
    prev = h

result = [x for row in board for x in row].count('#')
print(result)
