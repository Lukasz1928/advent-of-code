def read_input():
    with open('input', 'r') as f:
        return [tuple(line.split()) for line in f]


def score(opponent, player) -> int:
    return {
        'A': ['Z', 'X', 'Y'],
        'B': ['X', 'Y', 'Z'],
        'C': ['Y', 'Z', 'X'],
    }[opponent].index(player) * 3 + ['X', 'Y', 'Z'].index(player) + 1


data = read_input()
result = sum(score(*round) for round in data)
print(result)

