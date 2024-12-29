def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


def pad_input(d: list[str]) -> list[str]:
    return ['.' * (len(d[0]) + 2)] + [f'.{line}.' for line in d] + ['.' * (len(d[0]) + 2)]


data = pad_input(read_input())

to_check = {(x, y) for x in range(1, len(data) - 1) for y in range(1, len(data[0]) - 1)}

groups = []

neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while to_check:
    initial = to_check.pop()
    value = data[initial[0]][initial[1]]
    to_visit = [initial]
    visited = set()
    while to_visit:
        current = to_visit.pop()
        visited.add(current)
        for ngh in neighbours:
            ngh_loc = current[0] + ngh[0], current[1] + ngh[1]
            if data[ngh_loc[0]][ngh_loc[1]] == value and ngh_loc in to_check and ngh_loc not in to_visit:
                to_visit.append(ngh_loc)
                to_check.remove(ngh_loc)
    groups.append(visited)

result = 0


for group in groups:
    area = len(group)
    perimeter = sum(1 for item in group for ngh in neighbours if data[item[0]][item[1]] != data[item[0] + ngh[0]][item[1] + ngh[1]])
    result += area * perimeter

print(result)
