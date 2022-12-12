from collections import defaultdict, deque


def read_input() -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    data = []
    start = None
    end = None
    with open('input', 'r') as f:
        for line_idx, line in enumerate(f):
            data.append([])
            for col_idx, char in enumerate(line.strip()):
                if char.islower():
                    data[-1].append(ord(char) - ord('a'))
                elif char == 'S':
                    data[-1].append(0)
                    start = (line_idx, col_idx)
                else:  # char == 'E'
                    data[-1].append(ord('z') - ord('a'))
                    end = (line_idx, col_idx)
    return data, start, end


def build_graph(b: list[list[int]]) -> dict[tuple[int, int], set[tuple[int, int]]]:
    graph = defaultdict(set)
    changes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for line_idx, line in enumerate(b):
        for col_idx, val in enumerate(line):
            for dx, dy in changes:
                if 0 <= (x := line_idx + dx) < len(b) and 0 <= (y := col_idx + dy) < len(b[x]) and b[x][y] <= val + 1:
                    graph[(line_idx, col_idx)].add((x, y))
    return dict(graph)


def count_steps(g: dict[tuple[int, int], set[tuple[int, int]]], s: tuple[int, int], e: tuple[int, int]) -> int:
    to_visit = deque([(s, 0)])
    visited = set()
    awaiting = {s}
    while True:
        current, distance = to_visit.popleft()
        visited.add(current)
        awaiting.remove(current)
        if current == e:
            return distance
        for ngh in g[current]:
            if ngh not in visited and ngh not in awaiting:
                to_visit.append((ngh, distance + 1))
                awaiting.add(ngh)


board, start, end = read_input()
graph = build_graph(board)
result = count_steps(graph, start, end)
print(result)
