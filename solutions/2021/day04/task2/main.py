class Board:
    def __init__(self, board):
        self.board = board
        self.numbers = {number for row in board for number in row}

    @classmethod
    def from_raw(cls, data):
        lines = data.split('\n')
        return Board([[int(n) for n in l.split()] for l in lines])

    def _row_filled(self, numbers):
        for row in self.board:
            if set(row).issubset(numbers):
                return True
        return False

    def _column_filled(self, numbers):
        for column in [[r[i] for r in self.board] for i in range(5)]:
            if set(column).issubset(numbers):
                return True

    def is_winning(self, numbers):
        if len(numbers) < 5 or len(self.numbers.intersection(numbers)) < 5:
            return False
        return self._row_filled(numbers) or self._column_filled(numbers)

    def score(self, numbers):
        unmarked_numbers = self.numbers - set(numbers)
        return sum(unmarked_numbers) * numbers[-1]


def read_input():
    with open('input', 'r') as f:
        data = f.read().split('\n\n')
    numbers = [int(x) for x in data[0].split(',')]
    boards = [Board.from_raw(b) for b in data[1:]]
    return numbers, boards


def get_winning_boards(boards, numbers):
    return [b for b in boards if b.is_winning(numbers)]


numbers, boards = read_input()
result = None
last_winning = None, None
for i in range(len(numbers)):
    nums = numbers[:i + 1]
    bs = get_winning_boards(boards, nums)
    if not bs:
        continue
    for b in bs:
        boards.remove(b)
    last_winning = bs[-1], nums
result = last_winning[0].score(last_winning[1])
print(result)
