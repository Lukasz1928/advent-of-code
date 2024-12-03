def read_input() -> list[tuple[int, int]]:
    with open('input', 'r') as f:
        return [tuple(int(token) for token in line.split()) for line in f]


data = read_input()
sorted_left = sorted(item[0] for item in data)
sorted_right = sorted(item[1] for item in data)

result = sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))
print(result)
