from collections import Counter


def read_input() -> list[tuple[int, int]]:
    with open('input', 'r') as f:
        return [tuple(int(token) for token in line.split()) for line in f]


data = read_input()
right_counts = Counter(item[1] for item in data)

result = sum(item[0] * right_counts[item[0]] for item in data)
print(result)
