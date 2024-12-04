from re import findall


def read_input() -> str:
    with open('input', 'r') as f:
        return f.read()


data = read_input()
found = findall(r'mul\((\d+),(\d+)\)', data)
result = sum(int(token[0]) * int(token[1]) for token in found)
print(result)
