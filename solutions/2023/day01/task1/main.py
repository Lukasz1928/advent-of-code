from re import findall


def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


data = read_input()
result = 0
for line in data:
    numbers = findall(r'\d', line)
    result += 10 * int(numbers[0]) + int(numbers[-1])
print(result)
