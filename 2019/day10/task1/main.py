import math

board = [[e for e in row] for row in open('input', 'r').read().splitlines()]
empty_sign = '.'
asteroid_sign = '#'


class Direction:
    def __init__(self, x, y):
        gcd = math.gcd(abs(x), abs(y))
        self.x = (x // gcd) if gcd > 1 else x
        self.y = (y // gcd) if gcd > 1 else y

    def __eq__(self, other):
        if isinstance(other, Direction):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return 1000 * self.x + self.y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


def calculate_visible(board, x, y):
    directions = set()
    for p in range(len(board)):
        for q in range(len(board[i])):
            if board[p][q] == asteroid_sign and (x != p or y != q):
                dx, dy = x - p, y - q
                directions.add(Direction(dx, dy))
    return len(directions)


max_visible = -1
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == asteroid_sign:
            visible = calculate_visible(board, i, j)
            if visible > max_visible:
                max_visible = visible
print(max_visible)
