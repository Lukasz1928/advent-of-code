from math import log, ceil


def read_input() -> list[int]:
    with open('input', 'r') as f:
        return [int(x) for x in f.read().strip().split()]


def process_stone(value: int) -> list[int]:
    if value == 0:
        return [1]
    digits = ceil(log(value + 1, 10))
    if digits % 2 == 0:
        mul = 10 ** (digits // 2)
        l = value // mul
        r = value - l * mul
        return [l, r]
    return [value * 2024]


data = read_input()

for step in range(25):
    data = [elem for stone in data for elem in process_stone(stone)]

result = len(data)
print(result)
