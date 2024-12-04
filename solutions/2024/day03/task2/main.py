from re import findall


def read_input() -> str:
    with open('input', 'r') as f:
        return f.read()


data = read_input()
found = findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
is_enabled = True
result = 0
for item in found:
    if item == "do()":
        is_enabled = True
    elif item == "don't()":
        is_enabled = False
    elif is_enabled:
        tokens = item[4:-1].split(',')
        result += int(tokens[0]) * int(tokens[1])

print(result)
