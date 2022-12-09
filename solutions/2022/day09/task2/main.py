def read_input() -> list[tuple[str, int]]:
    with open('input', 'r') as f:
        return [((tokens := line.strip().split())[0], int(tokens[1])) for line in f]


changes = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


knots = [(0, 0)] * 10

visited = set()
instructions = read_input()
for instruction in instructions:
    direction, count = instruction
    change = changes[direction]
    for _ in range(count):
        knots[0] = (knots[0][0] + change[0], knots[0][1] + change[1])
        for i in range(1, 10):
            dx = knots[i - 1][0] - knots[i][0]
            dy = knots[i - 1][1] - knots[i][1]

            if abs(dx) >= 2 and dy == 0:
                knots[i] = (knots[i][0] + abs(dx) / dx, knots[i][1])
            elif dx == 0 and abs(dy) >= 2:
                knots[i] = (knots[i][0], knots[i][1] + abs(dy) / dy)
            elif abs(dx) >= 2 or abs(dy) >= 2:
                knots[i] = (knots[i][0] + abs(dx) / dx, knots[i][1] + abs(dy) / dy)
        visited.add(knots[9])
result = len(visited)
print(result)
