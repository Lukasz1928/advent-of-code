import re


def read_input():
    with open('input', 'r') as f:
        text = f.read()
    pattern = r'(row|column) (\d+)'
    matches = re.findall(pattern, text)
    if matches[0][0] == 'row':
        return [int(matches[0][1]), int(matches[1][1])]
    return [int(matches[1][1]), int(matches[0][1])]


def calculate_number_index(location):
    diagonal_id = location[0] + location[1] - 1
    numbers_on_previous_diagonals = diagonal_id * (diagonal_id - 1) // 2
    number_on_diagonal = location[1]
    return numbers_on_previous_diagonals + number_on_diagonal


def solve(location, start_value, mult, modulo):
    index = calculate_number_index(location)
    value = start_value
    for i in range(index - 1):
        value = (value * mult) % modulo
    return value


data = read_input()
result = solve(data, 20151125, 252533, 33554393)
print(result)
