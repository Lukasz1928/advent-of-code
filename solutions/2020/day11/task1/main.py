

def read_input():
    with open('input', 'r') as f:
        return [[x for x in line.strip()] for line in f]


def occupied_neighbors(board, x, y):
    return [p for row in board[max(0, x - 1):min(x + 2, len(board))]
            for p in row[max(0, y - 1):min(y + 2, len(row))]].count('#') - int(board[x][y] == '#')


def step(board):
    new_board = [[x for x in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            occ = occupied_neighbors(board, i, j)
            if board[i][j] == 'L' and occ == 0:
                new_board[i][j] = '#'
            elif board[i][j] == '#' and occ >= 4:
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
