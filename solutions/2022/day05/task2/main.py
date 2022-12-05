import re


def read_input() -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    with open('input', 'r') as f:
        raw_input = f.read()
    setup, moves = raw_input.split('\n\n')
    setup_lines = setup.split('\n')
    max_len = max(len(line) for line in setup_lines)

    columns = [[] for _ in range(max_len // 4 + 1)]
    for line in setup_lines[:-1]:
        for i in range(len(line) // 4 + 1):
            if (val := line[4 * i + 1]) != ' ':
                columns[i].append(val)
    moves_lines = moves.split('\n')
    lines = []
    for line in moves_lines:
        m = re.match(r'move (\d+) from (\d+) to (\d+)', line)
        lines.append((int(m.group(1)), int(m.group(2)) - 1, int(m.group(3)) - 1))
    return columns, lines


def move(current: list[list[str]], move_info: tuple[int, int, int]) -> list[list[str]]:
    count, source, target = move_info
    current[target] = current[source][:count] + current[target]
    current[source] = current[source][count:]
    return current


data, moves = read_input()
for m in moves:
    data = move(data, m)
result = ''.join([line[0] for line in data])
print(result)
