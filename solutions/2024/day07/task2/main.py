from math import log, ceil


def read_input() -> list[tuple[int, list[int]]]:
    d = []
    with open('input', 'r') as f:
        for line in f.readlines():
            tokens = line.strip().split(':')
            target = int(tokens[0])
            numbers = [int(num) for num in tokens[1].split()]
            d.append((target, numbers))
    return d


def number_ends_with(num: int, ends_with: int) -> bool:
    length = ceil(log(ends_with + 1, 10))
    return num % (10 ** length) == ends_with


def can_be_correct(target: int, numbers: list[int], last_index: int) -> bool:
    if last_index == 0:
        return numbers[0] == target
    if target % numbers[last_index] == 0 and can_be_correct(target // numbers[last_index], numbers, last_index - 1):
        return True
    if can_be_correct(target - numbers[last_index], numbers, last_index - 1):
        return True
    return number_ends_with(target, numbers[last_index]) and can_be_correct(target // (10 ** ceil(log(numbers[last_index] + 1, 10))), numbers, last_index - 1)


data = read_input()
result = sum(value[0] for value in data if can_be_correct(value[0], value[1], len(value[1]) - 1))
print(result)
