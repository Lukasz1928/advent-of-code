from re import findall, match


def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


def game_number_if_possible(row: str):
    game_number = int(match(r'Game (\d+):', row).group(1))

    games = row.split(':')[1]

    for game in games.split(';'):
        color_count = {'red': 12, 'green': 13, 'blue': 14}
        for cnt, color in findall('(\d+) (\w+)', game):
            color_count[color] -= int(cnt)
            if color_count[color] < 0:
                return 0
    return game_number


data = read_input()

result = 0
for row in data:
    result += game_number_if_possible(row)
print(result)
