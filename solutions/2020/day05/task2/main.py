
def read_input():
    with open('input', 'r') as f:
        return [line.strip() for line in f]


def seat_id(row, col):
    return 8 * row + col


def seat_row(seat):
    return int(''.join(str(int(d == 'B')) for d in seat[:7]), 2)


def seat_col(seat):
    return int(''.join(str(int(d == 'R')) for d in seat[7:]), 2)


passes = read_input()

ids = {seat_id(seat_row(s), seat_col(s)) for s in passes}
min_id, max_id = min(ids), max(ids)
empty_seat_id = [sid for sid in range(min_id, max_id + 1)
                 if sid not in ids and (sid + 1) in ids and (sid - 1) in ids][0]
print(empty_seat_id)
