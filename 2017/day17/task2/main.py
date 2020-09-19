def read_input():
    with open('input', 'r') as f:
        return int(f.read().strip())


steps = read_input()

pos = 0
next_number = 1
inserts = 50000000
result = 1
for i in range(inserts):
    pos = (pos + steps + 1) % next_number
    if pos == 0:
        result = next_number
    next_number += 1

print(result)
