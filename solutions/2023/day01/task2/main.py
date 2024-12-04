def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


data = read_input()
result = 0

numbers_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def to_number(x: str) -> int:
    if x.isdigit():
        return int(x)
    return numbers_names.index(x) + 1


def find_numbers(s: str) -> list[str]:
    result = []
    while s:
        for digit in list('0123456789') + numbers_names:
            if s.startswith(digit):
                result.append(digit)
        s = s[1:]
    return result


for line in data:
    numbers = find_numbers(line)
    result += 10 * to_number(numbers[0]) + to_number(numbers[-1])
print(result)
