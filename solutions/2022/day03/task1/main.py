def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


def get_score(line: str) -> int:
    repeated: str = set(line[:len(line)//2]).intersection(set(line[len(line)//2:])).pop()
    return (ord(repeated) - ord('a') + 1) if repeated.islower() else (ord(repeated) - ord('A') + 27)


data = read_input()
result = sum(get_score(line) for line in data)
print(result)
