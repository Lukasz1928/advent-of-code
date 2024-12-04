def read_input() -> list[list[int]]:
    with open('input', 'r') as f:
        return [[int(token) for token in line.split()] for line in f]


def is_save(row: list[int]) -> bool:
    if len(row) == 1:
        return True
    increasing = row[1] > row[0]
    for idx, item in enumerate(row[1:], start=1):
        if (increasing and item <= row[idx - 1]) or (not increasing and item >= row[idx - 1]) or abs(item - row[idx - 1]) > 3:
            return False
    return True


data = read_input()

result = sum(1 for row in data if is_save(row))
print(result)
