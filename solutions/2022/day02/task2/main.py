def read_input():
    with open('input', 'r') as f:
        return [tuple(line.split()) for line in f]


def score(opponent, player) -> int:
    return {
        'A': {'X': 3, 'Y': 1, 'Z': 2},
        'B': {'X': 1, 'Y': 2, 'Z': 3},
        'C': {'X': 2, 'Y': 3, 'Z': 1}
    }[opponent][player] + ['X', 'Y', 'Z'].index(player) * 3


data = read_input()
result = sum(score(*round) for round in data)
print(result)

