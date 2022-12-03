def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


def get_score(char: str) -> int:
    return (ord(char) - ord('a') + 1) if char.islower() else (ord(char) - ord('A') + 27)


data = read_input()
groups = [(set(data[3 * i]), set(data[3 * i + 1]), set(data[3 * i + 2])) for i in range(len(data) // 3)]
common = [g[0].intersection(g[1]).intersection(g[2]).pop() for g in groups]
result = sum(get_score(item) for item in common)
print(result)
