def read_input() -> list[list[int]]:
    with open('input', 'r') as f:
        return [[int(token) for token in line.split()] for line in f]


def is_increasing(row: list[int]) -> bool:
    if row[2] >= row[1] >= row[0]:
        return True
    if row[2] <= row[1] <= row[0]:
        return False
    if row[-3] >= row[-2] >= row[-1]:
        return False
    if row[-3] <= row[-2] <= row[-1]:
        return True
    raise ValueError()


def is_save(row: list[int]) -> bool:
    try:
        increasing = is_increasing(row)
    except ValueError:
        return False
    for remove_index in range(-1, len(row)):
        items = [elem for idx, elem in enumerate(row) if idx != remove_index]
        no_error = True
        for idx, item in enumerate(items[1:], start=1):
            if (increasing and item <= items[idx - 1]) or (not increasing and item >= items[idx - 1]) or abs(item - items[idx - 1]) > 3:
                no_error = False
                break
        if no_error:
            return True
    return False


data = read_input()

result = sum(1 for row in data if is_save(row))
print(result)
