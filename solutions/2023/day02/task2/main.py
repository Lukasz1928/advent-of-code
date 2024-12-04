from functools import reduce
from re import findall


def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


def powers(row: str):
    games = row.split(':')[1]
    necessary = {}
    for game in games.split(';'):
        color_count = {'red': 0, 'green': 0, 'blue': 0}
        for cnt, color in findall('(\d+) (\w+)', game):
            color_count[color] += int(cnt)
        for color, cnt in color_count.items():
            necessary[color] = max(necessary.get(color, 0), cnt)
    return reduce(lambda a, b: a * b, necessary.values())


data = read_input()

result = 0
for row in data:
    result += powers(row)
print(result)
