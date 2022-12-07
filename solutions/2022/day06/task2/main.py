

def read_input() -> str:
    with open('input', 'r') as f:
        return f.read().strip()


data = read_input()
distinct_chars_count = 14
result = None
for i in range(0, len(data) - distinct_chars_count):
    if len(set(data[i:i + distinct_chars_count])) == distinct_chars_count:
        result = i + distinct_chars_count
        break
print(result)
