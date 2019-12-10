import math

board = [[e for e in row] for row in open('input', 'r').read().splitlines()]
empty_sign = '.'
asteroid_sign = '#'


class Direction:
    def __init__(self, x, y, normalize=True):
        gcd = math.gcd(abs(x), abs(y))
        self.x = (x // gcd) if gcd > 1 and normalize else x
        self.y = (y // gcd) if gcd > 1 and normalize else y

    def __eq__(self, other):
        if isinstance(other, Direction):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return 1000 * self.x + self.y

    def __lt__(self, other):
        other_angle = math.atan2(other.y, other.x) + math.pi / 2.0
        this_angle = math.atan2(self.y, self.x) + math.pi / 2.0
        # if -math.pi/2.0 <= this_angle <= math.pi and not (-math.pi/2.0 <= other_angle <= math.pi):
        #     return False
        return this_angle > other_angle

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


def calculate_visible(board, x, y):
    directions = set()
    for p in range(len(board)):
        for q in range(len(board[i])):
            if board[p][q] == asteroid_sign and (x != p or y != q):
                dx, dy = p - x, q - y
                directions.add(Direction(dx, dy))
    return len(directions), list(sorted(directions))


def first_asteroid_in_direction(board, x, y, direction):
    dx, dy = direction.x, direction.y
    try:
        while 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
            if board[x + dx][y + dy] == asteroid_sign:
                return x + dx, y + dy
            dx += direction.x
            dy += direction.y
    except IndexError:
        pass
    return None, None

max_visible = -1
best_loc = None
visible = None
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == asteroid_sign:
            visible, _ = calculate_visible(board, i, j)
            if visible > max_visible:
                max_visible = visible
                best_loc = (i, j)

destroyed = 0
coords = None
while coords is None:
    _, directions = calculate_visible(board, best_loc[0], best_loc[1])
    for d in directions:
        target = first_asteroid_in_direction(board, best_loc[0], best_loc[1], d)
        if target[0] is not None:
            destroyed += 1
            board[target[0]][target[1]] = empty_sign
            if destroyed == 200:
                coords = (target[0], target[1])
                break
print(100 * coords[1] + coords[0])
