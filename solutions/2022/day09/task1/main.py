def read_input() -> list[tuple[str, int]]:
    with open('input', 'r') as f:
        return [((tokens := line.strip().split())[0], int(tokens[1])) for line in f]


changes = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


head = (0, 0)
tail = (0, 0)
visited = set()
instructions = read_input()
for instruction in instructions:
    direction, count = instruction
    change = changes[direction]
    for _ in range(count):
        head = (head[0] + change[0], head[1] + change[1])
        dx = head[0] - tail[0]
        dy = head[1] - tail[1]

        if abs(dx) >= 2 and dy == 0:
            tail = (tail[0] + abs(dx) / dx, tail[1])
        elif dx == 0 and abs(dy) >= 2:
            tail = (tail[0], tail[1] + abs(dy) / dy)
        elif abs(dx) >= 2 or abs(dy) >= 2:
            tail = (tail[0] + abs(dx) / dx, tail[1] + abs(dy) / dy)
        visited.add(tail)
result = len(visited)
print(result)
