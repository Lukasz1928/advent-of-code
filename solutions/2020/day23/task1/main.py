def read_input() -> list[int]:
    with open('input', 'r') as input_file:
        return [int(digit) for digit in input_file.read()]


def find_destination(cups: list[int], to_find: int) -> int:
    while True:
        to_find -= 1
        if to_find < min(cups):
            to_find = max(cups)
        try:
            return (cups.index(to_find)) % (len(cups))
        except ValueError:
            pass


def make_move(cups: list[int], current: int) -> tuple[list[int], int]:
    current_label = cups[current]
    removed = [cups[(current + offset) % len(cups)] for offset in range(1, 4)]
    step1 = [cup for cup in cups if cup not in removed]
    destination = find_destination(step1, current_label)
    step2 = step1[:(destination + 1) % (len(step1) + 1)] + removed + step1[(destination + 1) % (len(step1) + 1):]
    new_current = (step2.index(current_label) + 1) % len(cups)
    return step2, new_current


def calculate_result(cups: list[int]) -> str:
    one_idx = cups.index(1)
    return ''.join(str(cups[(one_idx + 1 + offset) % len(cups)]) for offset in range(len(cups) - 1))


data = read_input()
current_cup = 0
for step in range(100):
    data, current_cup = make_move(data, current_cup)

result = calculate_result(data)
print(result)
