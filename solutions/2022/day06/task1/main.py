

def read_input() -> str:
    with open('input', 'r') as f:
        return f.read().strip()


data = read_input()
result = None
for i in range(0, len(data) - 4):
    if len(set(data[i:i + 4])) == 4:
        result = i + 4
        break
print(result)
